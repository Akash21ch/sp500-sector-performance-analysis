import pandas as pd

# Load the file we just created
df = pd.read_excel("sector_data_raw.xlsx")

# Basic info
print("Shape of data (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nDate range:")
print("From:", df["Date"].min())
print("To:", df["Date"].max())

print("\nSectors in the data:")
print(df["Sector"].unique())

print("\nAny missing values?")
print(df.isnull().sum())