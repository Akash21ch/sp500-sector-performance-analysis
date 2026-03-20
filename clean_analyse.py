import pandas as pd

# Load the data
df = pd.read_excel("sector_data_raw.xlsx")

# Convert Date column to proper date format
df["Date"] = pd.to_datetime(df["Date"])

# Extract the year from the date
df["Year"] = df["Date"].dt.year

# -----------------------------------------------
# CALCULATE YEARLY RETURN FOR EACH SECTOR
# -----------------------------------------------
# For each sector, for each year:
# Get the first closing price and last closing price
# Return = ((Last Price - First Price) / First Price) * 100

yearly_returns = []

for sector in df["Sector"].unique():
    sector_df = df[df["Sector"] == sector]
    
    for year in sector_df["Year"].unique():
        year_df = sector_df[sector_df["Year"] == year].sort_values("Date")
        
        if len(year_df) < 2:
            continue
            
        first_price = year_df["Adjusted Close"].iloc[0]
        last_price = year_df["Adjusted Close"].iloc[-1]
        
        annual_return = ((last_price - first_price) / first_price) * 100
        
        yearly_returns.append({
            "Year": year,
            "Sector": sector,
            "Annual Return (%)": round(annual_return, 2)
        })

# Create a clean dataframe
returns_df = pd.DataFrame(yearly_returns)
returns_df = returns_df.sort_values(["Year", "Annual Return (%)"], ascending=[True, False])

# -----------------------------------------------
# SHOW BEST AND WORST SECTOR EACH YEAR
# -----------------------------------------------
print("BEST PERFORMING SECTOR EACH YEAR:")
print("=" * 50)
best = returns_df.groupby("Year").first().reset_index()
for _, row in best.iterrows():
    print(f"{int(row['Year'])}: {row['Sector']} ({row['Annual Return (%)']:+.1f}%)")

print("\nWORST PERFORMING SECTOR EACH YEAR:")
print("=" * 50)
worst = returns_df.groupby("Year").last().reset_index()
for _, row in worst.iterrows():
    print(f"{int(row['Year'])}: {row['Sector']} ({row['Annual Return (%)']:+.1f}%)")

# -----------------------------------------------
# SAVE THE CLEANED ANALYSIS FILE
# -----------------------------------------------
returns_df.to_excel("sector_yearly_returns.xlsx", index=False)
print("\n✅ Analysis saved to sector_yearly_returns.xlsx")


volatility = returns_df.groupby("Sector")["Annual Return (%)"].std().reset_index()
volatility.columns = ["Sector", "Volatility (Std Dev)"]
volatility = volatility.sort_values("Volatility (Std Dev)", ascending=False)
volatility["Volatility (Std Dev)"] = volatility["Volatility (Std Dev)"].round(2)

print("\nSECTOR VOLATILITY (Higher = More Risky):")
print("=" * 50)
for _, row in volatility.iterrows():
    print(f"{row['Sector']}: {row['Volatility (Std Dev)']}")

# Save to Excel
volatility.to_excel("sector_volatility.xlsx", index=False)
print("\n✅ Volatility data saved to sector_volatility.xlsx")