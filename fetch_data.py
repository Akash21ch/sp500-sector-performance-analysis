import requests
import pandas as pd
import time

# Your Alpha Vantage API key — paste it between the quotes
API_KEY = "YOUR_API_KEY_HERE"

# The 11 S&P 500 sectors and their ETF ticker symbols
sectors = {
    "Energy": "XLE",
    "Materials": "XLB",
    "Industrials": "XLI",
    "Utilities": "XLU",
    "Healthcare": "XLV",
    "Financials": "XLF",
    "Consumer Discretionary": "XLY",
    "Consumer Staples": "XLP",
    "Information Technology": "XLK",
    "Communication Services": "XLC",
    "Real Estate": "XLRE"
}

print("Downloading sector data... please wait")

all_data = []

for sector_name, ticker in sectors.items():
    print(f"Fetching {sector_name}...")
    
    url = (
        f"https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_MONTHLY_ADJUSTED"
        f"&symbol={ticker}"
        f"&apikey={API_KEY}"
        f"&datatype=json"
    )
    
    response = requests.get(url)
    data = response.json()
    
    # Check if we got data back
    if "Monthly Adjusted Time Series" not in data:
        print(f"⚠️ No data for {sector_name} — response: {data}")
        time.sleep(15)
        continue
    
    monthly = data["Monthly Adjusted Time Series"]
    
    rows = []
    for date_str, values in monthly.items():
        rows.append({
            "Date": date_str,
            "Open": float(values["1. open"]),
            "High": float(values["2. high"]),
            "Low": float(values["3. low"]),
            "Close": float(values["4. close"]),
            "Adjusted Close": float(values["5. adjusted close"]),
            "Volume": int(values["6. volume"]),
            "Sector": sector_name,
            "Ticker": ticker
        })
    
    df = pd.DataFrame(rows)
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Filter from year 2000 onwards
    df = df[df["Date"] >= "2000-01-01"]
    df = df.sort_values("Date")
    
    all_data.append(df)
    print(f"✅ {sector_name} — {len(df)} months of data")
    
    # Wait 12 seconds between calls (free tier allows 5 calls per minute)
    time.sleep(12)

# Combine all sectors
combined = pd.concat(all_data, ignore_index=True)

print(f"\nTotal rows: {len(combined)}")
print(f"Date range: {combined['Date'].min()} to {combined['Date'].max()}")
print(f"Sectors: {list(combined['Sector'].unique())}")

# Save to Excel
combined.to_excel("sector_data_raw.xlsx", index=False)
print("\n✅ Done! File saved as sector_data_raw.xlsx")