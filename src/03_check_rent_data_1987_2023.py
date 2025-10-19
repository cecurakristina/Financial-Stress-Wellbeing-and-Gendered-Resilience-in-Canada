import pandas as pd
import matplotlib.pyplot as plt

#load csv
raw_path = "data/raw/rent_avg_1987_2023.csv"
df = pd.read_csv(raw_path)

#keep only relevant columns (all data is referencing two bedroom units and apartment structures of six units and over)
df = df [["REF_DATE", "VALUE"]]
print(df.head())
print(df.info())

#remove rows with missing values
df = df.dropna(subset=["VALUE"])
print(df.info())

#rename columns
df = df.rename(columns={
    "REF_DATE": "year",
    "VALUE": "avg_rent_value"
})

print(df.head())

#remove 0 values
df = df[df["avg_rent_value"] > 0]
print(df.head())

#group values by year and calculate the median rent value for each year
df_yearly = df.groupby("year", as_index=False).median()
print(df_yearly.head())

#rename value
df_yearly = df_yearly.rename(columns={
    "avg_rent_value": "median_avg_rent_value"
})
print(df_yearly.head())

#save cleaned data
out_path = "data/processed/median-rent-clean-1987-2023.csv"
df_yearly.to_csv(out_path, index=False)
print("Saved cleaned data to:", out_path)

#plot trend over time
plt.figure(figsize=(10, 6))
plt.plot(df_yearly["year"], df_yearly["median_avg_rent_value"], marker='o', label="Median Average Rent for Two Bedroom Units in Apartment Structures of Six Units and Over")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Median Average Rent Value (Dollars)")
plt.title("Median Average Rent Trends (1987-2023)")
plt.grid(True)
plt.show()