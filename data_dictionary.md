# Bluestock Mutual Fund Analytics
## Data Dictionary

---

# 1. dim_fund

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| amfi_code | INTEGER | Unique AMFI Scheme Code | 01_fund_master.csv |
| fund_house | TEXT | Mutual Fund Company | 01_fund_master.csv |
| scheme_name | TEXT | Scheme Name | 01_fund_master.csv |
| category | TEXT | Fund Category | 01_fund_master.csv |
| sub_category | TEXT | Fund Sub Category | 01_fund_master.csv |
| plan | TEXT | Regular / Direct Plan | 01_fund_master.csv |
| launch_date | DATE | Scheme Launch Date | 01_fund_master.csv |
| benchmark | TEXT | Benchmark Index | 01_fund_master.csv |
| expense_ratio_pct | REAL | Expense Ratio (%) | 01_fund_master.csv |
| exit_load_pct | REAL | Exit Load (%) | 01_fund_master.csv |
| min_sip_amount | REAL | Minimum SIP Amount | 01_fund_master.csv |
| min_lumpsum_amount | REAL | Minimum Lump Sum Investment | 01_fund_master.csv |
| fund_manager | TEXT | Fund Manager | 01_fund_master.csv |
| risk_category | TEXT | Risk Category | 01_fund_master.csv |
| sebi_category_code | TEXT | SEBI Category Code | 01_fund_master.csv |

---

# 2. dim_date

| Column | Data Type | Description |
|----------|-----------|-------------|
| date | DATE | Calendar Date |
| year | INTEGER | Year |
| quarter | INTEGER | Quarter |
| month | INTEGER | Month Number |
| month_name | TEXT | Month Name |
| day | INTEGER | Day of Month |

---

# 3. fact_nav

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| nav_id | INTEGER | Primary Key | Generated |
| amfi_code | INTEGER | Fund Code | 02_nav_history.csv |
| date | DATE | NAV Date | 02_nav_history.csv |
| nav | REAL | Net Asset Value | 02_nav_history.csv |

---

# 4. fact_transactions

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| transaction_id | INTEGER | Primary Key | Generated |
| investor_id | TEXT | Investor ID | 08_investor_transactions.csv |
| transaction_date | DATE | Transaction Date | 08_investor_transactions.csv |
| amfi_code | INTEGER | Fund Code | 08_investor_transactions.csv |
| transaction_type | TEXT | SIP / Lumpsum / Redemption | 08_investor_transactions.csv |
| amount_inr | REAL | Transaction Amount | 08_investor_transactions.csv |
| state | TEXT | State | 08_investor_transactions.csv |
| city | TEXT | City | 08_investor_transactions.csv |
| city_tier | TEXT | T30 / B30 | 08_investor_transactions.csv |
| age_group | TEXT | Investor Age Group | 08_investor_transactions.csv |
| gender | TEXT | Investor Gender | 08_investor_transactions.csv |
| annual_income_lakh | REAL | Annual Income | 08_investor_transactions.csv |
| payment_mode | TEXT | Payment Method | 08_investor_transactions.csv |
| kyc_status | TEXT | KYC Verification Status | 08_investor_transactions.csv |

---

# 5. fact_performance

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| amfi_code | INTEGER | Fund Code | 07_scheme_performance.csv |
| scheme_name | TEXT | Scheme Name | 07_scheme_performance.csv |
| fund_house | TEXT | Fund House | 07_scheme_performance.csv |
| category | TEXT | Category | 07_scheme_performance.csv |
| plan | TEXT | Plan Type | 07_scheme_performance.csv |
| return_1yr_pct | REAL | 1-Year Return | 07_scheme_performance.csv |
| return_3yr_pct | REAL | 3-Year Return | 07_scheme_performance.csv |
| return_5yr_pct | REAL | 5-Year Return | 07_scheme_performance.csv |
| benchmark_3yr_pct | REAL | Benchmark Return | 07_scheme_performance.csv |
| alpha | REAL | Alpha | 07_scheme_performance.csv |
| beta | REAL | Beta | 07_scheme_performance.csv |
| sharpe_ratio | REAL | Sharpe Ratio | 07_scheme_performance.csv |
| sortino_ratio | REAL | Sortino Ratio | 07_scheme_performance.csv |
| std_dev_ann_pct | REAL | Annualized Standard Deviation | 07_scheme_performance.csv |
| max_drawdown_pct | REAL | Maximum Drawdown | 07_scheme_performance.csv |
| aum_crore | REAL | Assets Under Management | 07_scheme_performance.csv |
| expense_ratio_pct | REAL | Expense Ratio | 07_scheme_performance.csv |
| morningstar_rating | INTEGER | Morningstar Rating | 07_scheme_performance.csv |
| risk_grade | TEXT | Risk Grade | 07_scheme_performance.csv |

---

# 6. fact_aum

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| aum_id | INTEGER | Primary Key | Generated |
| date | DATE | Reporting Date | 03_aum_by_fund_house.csv |
| fund_house | TEXT | Fund House | 03_aum_by_fund_house.csv |
| aum_lakh_crore | REAL | AUM (Lakh Crore) | 03_aum_by_fund_house.csv |
| aum_crore | REAL | AUM (Crore) | 03_aum_by_fund_house.csv |
| num_schemes | INTEGER | Number of Schemes | 03_aum_by_fund_house.csv |

---

# 7. fact_sip

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| month | DATE | Month | 04_monthly_sip_inflows.csv |
| sip_inflow_crore | REAL | SIP Inflow | 04_monthly_sip_inflows.csv |
| active_sip_accounts_crore | REAL | Active SIP Accounts | 04_monthly_sip_inflows.csv |
| new_sip_accounts_lakh | REAL | New SIP Accounts | 04_monthly_sip_inflows.csv |
| sip_aum_lakh_crore | REAL | SIP AUM | 04_monthly_sip_inflows.csv |
| yoy_growth_pct | REAL | YoY Growth (%) | 04_monthly_sip_inflows.csv |

---

# 8. fact_category_inflows

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| id | INTEGER | Primary Key | Generated |
| month | DATE | Month | 05_category_inflows.csv |
| category | TEXT | Mutual Fund Category | 05_category_inflows.csv |
| net_inflow_crore | REAL | Net Inflow | 05_category_inflows.csv |