# S&P 500 Sector Performance Analysis (2000–2026)

## Overview
An end-to-end data analysis project examining the performance of all 11 S&P 500 sectors over 25 years (2000–2026), built using Python, Alpha Vantage API and Tableau Public.

## Live Dashboard
👉 [View Interactive Tableau Dashboard](https://public.tableau.com/app/profile/akash.chaudhary4621/viz/SP500-Sector-Performance-Analysis/Dashboard1)

## Key Questions Answered
- Which S&P 500 sector performed best each year?
- Which sectors were most volatile and risky?
- How did sectors perform during major events like the 2008 financial crisis and COVID-19?

## Tools & Technologies
- Python (pandas, requests)
- Alpha Vantage API
- Tableau Public
- Microsoft Excel

## Project Structure
- `fetch_data.py` — Fetches real financial data from Alpha Vantage API
- `explore_data.py` — Initial data exploration and validation
- `clean_analyse.py` — Data cleaning, annual return calculations and volatility analysis
- `sector_yearly_returns.xlsx` — Cleaned yearly returns by sector
- `sector_volatility.xlsx` — Volatility rankings by sector

## Key Findings
- Information Technology was the most volatile sector (std dev: 26.59)
- Consumer Staples was the most stable sector (std dev: 11.23)
- Financials suffered the worst single year return in 2008 (-55.3%) during the financial crisis
- Information Technology dominated returns in 2019, 2020 and 2023
- Energy was the best performing sector in 2021 and 2022 post-COVID recovery

## How to Run
1. Clone this repository
2. Get a free API key from Alpha Vantage
3. Replace YOUR_API_KEY_HERE in fetch_data.py with your key
4. Install dependencies: pip install pandas requests openpyxl
5. Run fetch_data.py to download data
6. Run clean_analyse.py to generate analysis

## Author
Akash Chaudhary | [GitHub](https://github.com/Akash21ch)
