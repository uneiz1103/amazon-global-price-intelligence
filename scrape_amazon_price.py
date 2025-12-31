import pandas as pd
import time
import random
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
def init_driver():
    options = Options()
    options.add_argument("--headless=new")  # modern headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Extract ONLY BuyBox Price
def get_buybox_price(driver, asin):
    url = f"https://www.amazon.in/dp/{asin}"
    # url = f"https://www.amazon.sa/dp/{asin}"
    # url = f"https://www.amazon.co.uk/dp/{asin}"
    # url = f"https://www.amazon.com.au/dp/{asin}"
    driver.get(url)
    time.sleep(random.uniform(3, 6))

    try:
        buybox_container = driver.find_element(By.ID, "buybox")  # If BuyBox exists
        price_element = buybox_container.find_element(By.CSS_SELECTOR, "span.a-price span.a-offscreen")
        price = price_element.get_attribute("innerText").strip()
    except:
        price = "Not Found"

    return price

def clean_headers(df):
    df.columns = df.columns.map(lambda x: str(x).strip().replace("\n", "").replace("\r", ""))
    return df

# Main Function
def update_excel(file_path):
    try:
        df = pd.read_excel(file_path, dtype=str, engine='openpyxl')
        df = clean_headers(df)
    except Exception as e:
        print("Failed to read Excel file:", e)
        return

    print("Columns found in Excel:", df.columns.tolist())

    if "ASIN" not in df.columns:
        print("Error: 'ASIN' column not found in the Excel file.")
        return

    df["ASIN"] = df["ASIN"].astype(str).str.strip()
    asins = df["ASIN"].dropna().tolist()

    driver = init_driver()

    for index, asin in enumerate(asins):
        price = get_buybox_price(driver, asin)
        df.at[index, "Price"] = price
        print(f"{index+1}/{len(asins)} - ASIN: {asin} | Price: {price}")
        time.sleep(random.uniform(2.5, 5))

    driver.quit()

    output_file = file_path.replace(".xlsx", "_output.xlsx")
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"\n Done! Results saved to: {output_file}")


if __name__ == "__main__":
    file_path = "asin_list.xlsx"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
    else:
        update_excel(file_path)
