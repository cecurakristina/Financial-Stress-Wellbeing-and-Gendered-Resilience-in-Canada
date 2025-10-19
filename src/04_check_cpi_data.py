import pandas as pd
import matplotlib.pyplot as plt

#load csv
raw_path = "data/raw/cpi_all_items.csv"
df = pd.read_csv(raw_path)

#look at the data
print(df.head())

#keep only relevant columns
df = df[["REF_DATE", "VALUE"]]

#rename columns
df = df.rename(columns={
    "REF_DATE": "year",
    "VALUE": "cpi_value"
})
print(df.head())
#check for missing values and data types
print(df.info())
#no missing values found, data types look good

#save cleaned data
out_path = "data/processed/cpi-clean-all-items.csv"
df.to_csv(out_path, index=False)
print("Saved cleaned data to:", out_path)

#plot CPI over time to ensure data looks correct
plt.figure(figsize=(10, 6))
plt.plot(df["year"], df["cpi_value"], marker='o', label="CPI All Items Canada")
plt.legend()
plt.xlabel("Year")
plt.ylabel("CPI Value")
plt.title("Consumer Price Index (CPI) All Items Over Time")
plt.grid(True)
plt.show()