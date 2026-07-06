"""
Load cleaned datasets into SQLite database
Bluestock Mutual Fund Analytics
"""

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE = BASE_DIR / "data" / "db" / "bluestock_mf.db"
PROCESSED = BASE_DIR / "data" / "processed"

engine = create_engine(f"sqlite:///{DATABASE}")

print("=" * 70)
print("Loading Cleaned Data into SQLite")
print("=" * 70)

# ==========================================================
# Dataset Mapping
# ==========================================================

datasets = [
    ("clean_01_fund_master.csv", "dim_fund"),
    ("clean_02_nav_history.csv", "fact_nav"),
    ("clean_03_aum_by_fund_house.csv", "fact_aum"),
    ("clean_04_monthly_sip_inflows.csv", "fact_sip"),
    ("clean_05_category_inflows.csv", "fact_category_inflows"),
    ("clean_07_scheme_performance.csv", "fact_performance"),
    ("clean_08_investor_transactions.csv", "fact_transactions"),
]

# ==========================================================
# Load each dataset
# ==========================================================

for filename, table in datasets:

    filepath = PROCESSED / filename

    print(f"\nLoading {filename}")

    df = pd.read_csv(filepath)

    # Remove auto-generated ID columns because SQLite creates them
    if table == "fact_nav":
        pass

    elif table == "fact_transactions":
        pass

    elif table == "fact_aum":
        pass

    elif table == "fact_performance":
        pass

    # Load into SQLite
    df.to_sql(
        table,
        engine,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(df)} rows into {table}")

print("\nAll datasets loaded successfully.")