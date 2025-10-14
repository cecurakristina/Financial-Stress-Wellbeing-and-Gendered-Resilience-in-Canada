import pandas as pd
import matplotlib.pyplot as plt

#read the csv file
raw_path = "data/raw/2000-2023-income.csv"
df = pd.read_csv(raw_path)

print(df)

#keep only the relevant columns
df = df[['REF_DATE', 'Family characteristics', 'VALUE']]

#rename columns
df = df.rename(columns={
    'REF_DATE': 'year',
    'Family characteristics': 'family_income_type',
    'VALUE': 'income_value'
})

#check unique values in 'family_income_type' column
measures = df['family_income_type'].unique()
print("Measures available:", measures)

#drop unnecessary measures
measures_to_drop = [
    'Median total income, couple families',
    'Median total income, one-parent families'
]

df = df[~df['family_income_type'].isin(measures_to_drop)].copy()

#reassign measures variable to see remaining measures
measures = df['family_income_type'].unique()
print("Measures available:", measures)

#check for missing values and data types
print(df.info())
#no missing values found, data types look good

print(df)

#pivot the dataframe to have years as rows and income types as columns
df_wide = df.pivot_table(index='year', columns='family_income_type', values='income_value').reset_index()
df_wide = df_wide.rename(columns={
    'Median total income, all families': 'median_total_all_families',
    'Median employment income of dual-earner couple families': 'median_emp_dual_earner',
    'Median employment income of single-earner-male couple families': 'median_emp_single_male',
    'Median employment income of single-earner-female couple families': 'median_emp_single_female'
})
print(df_wide)

#check year range
print("Year range:", df_wide['year'].min(), "-", df_wide['year'].max())

#create a simple derived column: dual-earner / single-earner-female ratio
df_wide['ratio_dual_to_single_female'] = df_wide['median_emp_dual_earner'] / df_wide['median_emp_single_female']

#check the summary statistics
print(df_wide.describe())

#save the cleaned data
out_path = "data/processed/median_income_clean_2000_2023.csv"
df_wide.to_csv(out_path, index=False)
print("Saved cleaned file to:", out_path)

#plot the trends over time
plt.figure(figsize=(9,5))
plt.plot(df_wide['year'], df_wide['median_emp_dual_earner'], marker='o', label='Median employment income (dual-earner families)')
plt.plot(df_wide['year'], df_wide['median_total_all_families'], marker='o', label='Median total income (all families)')
plt.plot(df_wide['year'], df_wide['median_emp_single_male'], marker='o', label='Median employment income (single-earner male)')
plt.plot(df_wide['year'], df_wide['median_emp_single_female'], marker='o', label='Median employment income (single-earner female)')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Income')
plt.title('Median income trends (2000–2023)')
plt.grid(True)
plt.show()