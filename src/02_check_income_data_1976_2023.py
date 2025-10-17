import pandas as pd
import matplotlib.pyplot as plt

#load csv
raw_path = "data/raw/1976-2023-income.csv"
df = pd.read_csv(raw_path)

#look at the data
print(df.head())

#keep only relevant columns
df = df[["REF_DATE", "Economic family type", "VALUE"]]

#rename columns
df = df.rename(columns={
    "REF_DATE": "year",
    "Economic family type": "family_type",
    "VALUE": "income_value"
})

#check unique values
family_type_measure = df["family_type"].unique()
print("Family types available:", family_type_measure)

#check for missing values and data types
print(df.info())
#no missing values found, data types look good

#pivot the dataframe to have years as rows and family types as columns
df_wide = df.pivot_table(index="year", columns="family_type", values="income_value").reset_index()
print (df_wide)

#check year range
print("Year range is: ", df_wide["year"].min(), "-", df_wide["year"].max())

#check the summary statistics
print(df_wide.describe())

#save cleaned data
out_path = "data/processed/median-income-clean-1976-2023.csv"
df_wide.to_csv(out_path, index=False)
print("Saved cleaned data to:", out_path)

#plot trends over time for different family types
plt.figure(figsize=(10, 6))
plt.plot(df_wide["year"], df_wide["Economic families"], marker='o', label="Median Total Income Economic Families")
plt.plot(df_wide["year"], df_wide["Persons not in an economic family"], marker='o', label="Median Total Income Non-Economic Families")
plt.plot(df_wide["year"], df_wide["Economic families and persons not in an economic family"], marker='o', label="Median Total Income All Families")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Income Value")
plt.title("Median Income Trends by Family Type (1976-2023)")
plt.grid(True)
plt.show()