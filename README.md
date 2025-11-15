# Do Two Incomes Buy What One Did?
A data analysis of income, rent, and purchasing power in Canada

This project examines how purchasing power and affordability have changed in Canada over the past four decades. Using Statistics Canada datasets and the Consumer Price Index (CPI), the analysis evaluates trends in median income, average rent, inflation‑adjusted real values, and the gender wage gap.

The central question: Do two incomes today buy what one income used to?

---

## Key Findings

### Purchasing Power Decline
- Real (CPI‑adjusted) median income in 2023 is approximately 41% lower than its inflation‑adjusted level in the 1980s.

### Housing Affordability
- Nominal rent nearly tripled from 1987 to 2023.  
- After adjusting for inflation, real rent increased by about 25%.

### Rent Burden Shifts
- 1987 single‑earner: ~15% of income went to rent.  
- 2023 single‑earner: ~32% of income goes to rent.  
- 2023 dual‑income household: ~12% goes to rent - close to the 1987 single‑income burden.

### Gender Wage Gap
- Pay ratio improved from 1.78 in 2000 to 1.26 in 2023.  
- Women still earn ~26% less on average.

---

## Technologies Used
- Python (pandas, matplotlib)  
- Jupyter Notebook  
- Power BI (data modeling, DAX, dashboard design)  
- Git & GitHub  
- Statistics Canada datasets

---

## Repository Structure

└───canadian-housing-and-income-trends
    │   README.md
    │
    ├───dashboards
    │   │   Financial_Decline_Dashboards.pbix
    │   │
    │   └───screenshots
    │           2-Incomes-VS-1-Income.png
    │           CPI-Adjusted-Rent-Income.png
    │           Male-Female-Income.png
    │           Male-Female-Ratio.png
    │           Percentage-Change.png
    │           Purchasing-Power-Income.png
    │
    ├───data
    │   ├───processed
    │   │       cpi-clean-all-items.csv
    │   │       gender_gap_ratios_2000_2023.csv
    │   │       income_rent_1987_2023_combined.csv
    │   │       median-income-clean-1976-2023.csv
    │   │       median-income-clean-2000-2023.csv
    │   │       median-rent-clean-1987-2023.csv
    │   │
    │   └───raw
    │           1976-2023-income.csv
    │           2000-2023-income.csv
    │           cpi_all_items.csv
    │           rent_avg_1987_2023.csv
    │
    ├───reports
    │       Final_Report.pdf
    │
    └───src
            01_check_income_data_2000_2023.py
            02_check_income_data_1976_2023.py
            03_check_rent_data_1987_2023.py
            04_check_cpi_data.py
            05_cpi_adjustment.py
            06_exploratory_analysis.ipynb
            07_prepare_powerbi_datasets.py

---

## Project Deliverables
- Cleaned datasets: processed CSV files with inflation‑adjusted values, derived metrics, and merged datasets.  
- Exploratory analysis: notebook including CPI adjustment, trend analysis, income/rent comparisons, gender wage gap, summary tables and visualizations.  
- Power BI dashboard: five‑page dashboard covering income and rent trends and gender wage gap
- Final report: structured analysis summarizing data and methods, findings, discussion, conclusion and next steps.

---

## Data Sources
- Statistics Canada. (2024). Income statistics by economic family type and income source, 1976–2023 (Table 11-10-0190-01; formerly CANSIM 206-0021).
- Statistics Canada. (2024). Selected income characteristics of census families by family type, 2000–2023 (Table 11-10-0009-01; formerly CANSIM 111-0009).
- Statistics Canada; Canada Mortgage and Housing Corporation. (2024). Average rents for areas with a population of 10,000 and over, 1987–2023 (Table 34-10-0133-01; formerly CANSIM 027-0040).
- Statistics Canada. (2024). Consumer Price Index, annual average, not seasonally adjusted (Table 18-10-0005-01; formerly CANSIM 326-0021).


---

## Skills Demonstrated
- Data cleaning and preprocessing  
- Exploratory data analysis  
- CPI‑based inflation adjustment  
- Creating derived metrics and ratios  
- Power BI modeling and DAX  
- Data visualization and storytelling  
- Reproducible project structuring  
- Version control (Git, GitHub)

---

## Future Work
Originally, this project included a mental health and wellbeing component. Possible extensions:
- Financial stress and self‑reported mental health analysis  
- Gendered patterns in job satisfaction and workload  
- Policy evaluation (leave policies, pay transparency, etc.)