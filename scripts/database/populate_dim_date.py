"""
Populate dim_date table from all date columns
"""

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# ======================================================
# Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE = BASE_DIR / "data" / "db" / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DATABASE}")

print("=" * 70)
print("Populating dim_date")
print("=" * 70)

# ------------------------------------------------------
# Read dates from database
# ------------------------------------------------------

nav = pd.read_sql("SELECT date FROM fact_nav", engine)

txn = pd.read_sql(
    "SELECT transaction_date AS date FROM fact_transactions",
    engine
)

aum = pd.read_sql(
    "SELECT date FROM fact_aum",
    engine
)

# ------------------------------------------------------
# Combine dates
# ------------------------------------------------------

dates = pd.concat([nav, txn, aum])

dates["date"] = pd.to_datetime(dates["date"])

dates = dates.drop_duplicates()

dates = dates.sort_values("date")

# ------------------------------------------------------
# Create Date Dimension
# ------------------------------------------------------

dates["year"] = dates["date"].dt.year

dates["quarter"] = dates["date"].dt.quarter

dates["month"] = dates["date"].dt.month

dates["month_name"] = dates["date"].dt.month_name()

dates["day"] = dates["date"].dt.day

# ------------------------------------------------------
# Save
# ------------------------------------------------------

dates.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)

print(f"Inserted {len(dates)} dates.")
print("\nDone.")