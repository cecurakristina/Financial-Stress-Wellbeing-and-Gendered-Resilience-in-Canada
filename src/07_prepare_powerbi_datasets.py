import pandas as pd

# Load processed datasets
income_path = "data/processed/median-income-clean-1976-2023.csv"
rent_path = "data/processed/median-rent-clean-1987-2023.csv"
cpi_path = "data/processed/cpi-clean-all-items.csv"
gender_path = "data/processed/median-income-clean-2000-2023.csv"

income_df = pd.read_csv(income_path)
rent_df = pd.read_csv(rent_path)
cpi_df = pd.read_csv(cpi_path)
gender_df = pd.read_csv(gender_path)

# Prepare income + rent merged dataset (1987–2023)
income_1987 = income_df[income_df["year"] >= 1987]
merged = income_1987.merge(rent_df, on="year", how="inner")
merged = merged.merge(cpi_df, on="year", how="left")

# Calculate CPI-adjusted (real) income and rent
base_cpi = cpi_df.loc[cpi_df["year"] == 2023, "cpi_value"].values[0]
merged["real_income_2023"] = merged["Economic families"] * (base_cpi / merged["cpi_value"])
merged["real_rent_2023"] = merged["median_avg_rent_value"] * (base_cpi / merged["cpi_value"])

# Rent-to-income ratio
merged["rent_to_income_ratio"] = merged["real_rent_2023"] / merged["real_income_2023"]

# Save for Power BI
merged_out = "data/processed/income_rent_1987_2023_combined.csv"
merged.to_csv(merged_out, index=False)
print("Saved:", merged_out)

# Prepare gender gap ratios dataset
gender_df["ratio_male_to_female"] = gender_df["median_emp_single_male"] / gender_df["median_emp_single_female"]
gender_out = "data/processed/gender_gap_ratios_2000_2023.csv"
gender_df.to_csv(gender_out, index=False)
print("Saved:", gender_out)
