# Amazon Global Price Intelligence

## Overview
This project automates the extraction of Amazon BuyBox prices across different countries to support **cross-market pricing analysis**, **competitive benchmarking**, and **profit margin evaluation**.

Amazon seller accounts typically expose pricing data only for the registered marketplace.  
This solution enables visibility into **international pricing trends**, helping businesses that source products from India and sell globally make **data-driven pricing decisions**.

---

## Business Problem
Our business purchases products from India and sells them in multiple international markets.  
However:
- Amazon provides seller price visibility only for the country of account registration
- Cross-country competitor prices are not directly accessible
- Manual price checks are time-consuming and unreliable

This project addresses these challenges by automating **BuyBox price extraction** for multiple Amazon marketplaces.

---

## Solution Approach
- Automated Amazon product page access using Selenium
- BuyBox-focused price extraction for accurate market pricing
- Country-specific marketplace support (IN, UK, SA, AU, etc.)
- Structured Excel-based input and output for analyst-friendly workflows
- Randomized delays and headless browsing for stability

---

## Key Features
- Extracts **BuyBox price only** (primary seller price)
- Supports multiple Amazon marketplaces by switching domain
- Reads ASINs directly from Excel input
- Outputs clean, structured Excel files for analysis
- Designed for pricing, margin, and market comparison analysis

---

## Tech Stack
- **Python**
- **Pandas** – data handling and transformation
- **Selenium** – browser automation
- **Chrome WebDriver (Headless)**
- **Excel (openpyxl)** – analyst-friendly input/output

---

## Workflow
1. Analyst provides ASIN list in Excel
2. Script navigates to Amazon product pages
3. BuyBox price is extracted per ASIN
4. Prices are appended to the dataset
5. Clean output file is generated for analysis

---

## Input File Format
**asin_list.xlsx**
| ASIN |
|------|
| B08XXXXXX |
| B09XXXXXX |

---

## Output File
**asin_list_output.xlsx**

Includes:
- ASIN
- Extracted BuyBox Price

Ready for:
- Margin calculations
- Cross-country comparison
- Dashboarding (Power BI / Excel)

---

## Use Cases
- Cross-country price benchmarking
- Profit margin estimation
- Competitive analysis
- International pricing strategy
- Market intelligence reporting

---

## Ethical & Compliance Note
This project is intended strictly for **internal business analysis and pricing intelligence**.  
All requests are rate-limited with randomized delays to minimize server load.

---

## Author
**Data Analyst**  
Focused on building real-world, business-driven data pipelines for pricing and market intelligence.
