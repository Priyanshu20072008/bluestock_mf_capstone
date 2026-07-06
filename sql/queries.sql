
-- Query 1: Top 5 Funds by AUM

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

----------------------------------------------------------

-- Query 2: Average NAV Per Month

SELECT
    d.year,
    d.month_name,
    ROUND(AVG(f.nav), 2) AS average_nav
FROM fact_nav f
JOIN dim_date d
ON f.date = d.date
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

----------------------------------------------------------

-- Query 3: SIP YoY Growth

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip
ORDER BY month;

----------------------------------------------------------

-- Query 4: Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

----------------------------------------------------------

-- Query 5: Funds with Expense Ratio Less Than 1%

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

----------------------------------------------------------

-- Query 6: Top 10 Funds by 5-Year Return

SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

----------------------------------------------------------

-- Query 7: Average Transaction Amount by Payment Mode

SELECT
    payment_mode,
    ROUND(AVG(amount_inr),2) AS average_amount
FROM fact_transactions
GROUP BY payment_mode
ORDER BY average_amount DESC;

----------------------------------------------------------

-- Query 8: Investor Count by Gender

SELECT
    gender,
    COUNT(*) AS investors
FROM fact_transactions
GROUP BY gender;

----------------------------------------------------------

-- Query 9: Total AUM by Fund House

SELECT
    fund_house,
    ROUND(SUM(aum_crore),2) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

----------------------------------------------------------

-- Query 10: Average NAV by Fund

SELECT
    f.scheme_name,
    ROUND(AVG(n.nav),2) AS average_nav
FROM fact_nav n
JOIN dim_fund f
ON n.amfi_code = f.amfi_code
GROUP BY f.scheme_name
ORDER BY average_nav DESC;