-- =====================================================
-- Bluestock Mutual Fund Analytics Database
-- =====================================================

DROP TABLE IF EXISTS fact_nav;
DROP TABLE IF EXISTS fact_transactions;
DROP TABLE IF EXISTS fact_performance;
DROP TABLE IF EXISTS fact_aum;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_fund;

--------------------------------------------------------
-- Dimension Table : Fund
--------------------------------------------------------

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date DATE,
    benchmark TEXT,

    expense_ratio_pct REAL,

    exit_load_pct REAL,

    min_sip_amount REAL,

    min_lumpsum_amount REAL,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT

);

--------------------------------------------------------
-- Dimension Table : Date
--------------------------------------------------------

CREATE TABLE dim_date(

    date DATE PRIMARY KEY,

    year INTEGER,

    quarter INTEGER,

    month INTEGER,

    month_name TEXT,

    day INTEGER

);

--------------------------------------------------------
-- Fact : NAV
--------------------------------------------------------

CREATE TABLE fact_nav(

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    date DATE,

    nav REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY(date)
        REFERENCES dim_date(date)

);

--------------------------------------------------------
-- Fact : Investor Transactions
--------------------------------------------------------

CREATE TABLE fact_transactions(

    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id TEXT,

    transaction_date DATE,

    amfi_code INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)

);

--------------------------------------------------------
-- Fact : Scheme Performance
--------------------------------------------------------

CREATE TABLE fact_performance(

    amfi_code INTEGER PRIMARY KEY,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    plan TEXT,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    aum_crore REAL,

    expense_ratio_pct REAL,

    morningstar_rating INTEGER,

    risk_grade TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)

);

--------------------------------------------------------
-- Fact : AUM
--------------------------------------------------------

CREATE TABLE fact_aum(

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date DATE,

    fund_house TEXT,

    aum_lakh_crore REAL,

    aum_crore REAL,

    num_schemes INTEGER

);
--------------------------------------------------------
-- Fact : Monthly SIP Inflows
--------------------------------------------------------

CREATE TABLE fact_sip (

    month DATE PRIMARY KEY,

    sip_inflow_crore REAL,

    active_sip_accounts_crore REAL,

    new_sip_accounts_lakh REAL,

    sip_aum_lakh_crore REAL,

    yoy_growth_pct REAL

);

--------------------------------------------------------
-- Fact : Category Inflows
--------------------------------------------------------

CREATE TABLE fact_category_inflows (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    month DATE,

    category TEXT,

    net_inflow_crore REAL

);