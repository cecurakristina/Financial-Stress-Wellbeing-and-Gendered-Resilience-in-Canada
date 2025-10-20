import pandas as pd
import matplotlib.pyplot as plt

#load cleaned datsasets
income_path = "data/processed/median-income-clean-1976-2023.csv"
rent_path = "data/processed/median-rent-clean-1987-2023.csv"
cpi_path = "data/processed/cpi-clean-all-items.csv"

income = pd.read_csv(income_path)
rent = pd.read_csv(rent_path)
cpi = pd.read_csv(cpi_path)

#look at cpi data
print(cpi)

#get base cpi value for 2023
base_cpi = cpi.loc[cpi["year"] == 2023, "cpi_value"].values[0]
print("Base CPI for 2023:", base_cpi)

#merge cpi with income 
income_merged = pd.merge(income, cpi, on="year", how="left")
#calculate real income in 2023 dollars
for col in ["Economic families", 
            "Persons not in an economic family", 
            "Economic families and persons not in an economic family"]:
        income_merged[f"{col} adjusted"] = income_merged[col] * (base_cpi / income_merged["cpi_value"])
print(income_merged)

#merge cpi with rent
rent_merged = pd.merge(rent, cpi, on="year", how="left")
#calculate real rent in 2023 dollars
rent_merged["median_avg_rent_value_adjusted"] = rent_merged["median_avg_rent_value"] * (base_cpi / rent_merged["cpi_value"])
print(rent_merged)

#plot adjusted income trends for economic families and adjusted rent
plt.figure(figsize=(10, 6))
plt.plot(income_merged["year"], income_merged["Economic families adjusted"], marker='o', label="Median Total Income Economic Families (2023 $)")
plt.plot(rent_merged["year"], rent_merged["median_avg_rent_value_adjusted"], marker='o', label="Median Average Rent (2023 $)")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Value in 2023 Dollars")
plt.title("Adjusted Median Income and Rent Trends (1976-2023)")
plt.grid(True)
plt.show()
