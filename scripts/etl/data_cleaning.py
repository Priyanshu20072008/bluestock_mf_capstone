# """
# Day 2 - Data Cleaning
# Bluestock Mutual Fund Analytics
# """

# from pathlib import Path
# import pandas as pd

# BASE_DIR = Path(__file__).resolve().parents[2]

# RAW = BASE_DIR / "data" / "raw"
# PROCESSED = BASE_DIR / "data" / "processed"

# PROCESSED.mkdir(exist_ok=True)

# print("=" * 70)
# print("Bluestock Data Cleaning")
# print("=" * 70)

# # Load NAV History
# nav = pd.read_csv(RAW / "02_nav_history.csv")

# print(nav.head())
# print(nav.info())

# #Convert Date Column
# nav["date"] = pd.to_datetime(nav["date"])

# print(nav.dtypes)
# #Sort Data
# nav = nav.sort_values(
#     by=["amfi_code", "date"]
# )

# # Remove Duplicates
# before = len(nav)

# nav = nav.drop_duplicates()

# after = len(nav)

# print(f"Duplicates Removed : {before-after}")

# # Missing Values
# print(nav.isnull().sum())

# #Forward Fill Missing NAV
# nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# #Validate NAV
# invalid = nav[nav["nav"] <= 0]

# print("Invalid NAV values:", len(invalid))

# #Save Clean Dataset
# nav.to_csv(
#     PROCESSED / "clean_nav_history.csv",
#     index=False
# )

# print("Clean NAV saved.")
"""
Day 2 - Data Cleaning
Bluestock Mutual Fund Analytics Platform

Author: Priyanshu
"""

from pathlib import Path
import pandas as pd
from pandas.api.types import is_numeric_dtype

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

RAW = BASE_DIR / "data" / "raw"
PROCESSED = BASE_DIR / "data" / "processed"
REPORTS = BASE_DIR / "reports"

# Create folders if they don't exist
PROCESSED.mkdir(exist_ok=True)
REPORTS.mkdir(exist_ok=True)

print("=" * 70)
print("Bluestock Mutual Fund Data Cleaning Pipeline")
print("=" * 70)

# ==========================================================
# Get all CSV files
# ==========================================================

csv_files = sorted(RAW.glob("*.csv"))

summary = []

# ==========================================================
# Process each dataset
# ==========================================================

for file in csv_files:

    print(f"\nProcessing: {file.name}")

    # ---------------------------
    # Load CSV
    # ---------------------------

    df = pd.read_csv(file)

    rows_before = len(df)

    # ---------------------------
    # Remove duplicate rows
    # ---------------------------

    duplicate_rows = df.duplicated().sum()
    df = df.drop_duplicates()

    # ---------------------------
    # Convert date columns
    # ---------------------------

    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

    # ---------------------------
    # Handle Missing Values
    # ---------------------------

    for col in df.columns:

        if is_numeric_dtype(df[col]):
            median_value = df[col].median()

            if pd.notna(median_value):
                df[col] = df[col].fillna(median_value)

        else:
            df[col] = df[col].fillna("Unknown")

# ---------------------------
# Dataset Specific Validation
# ---------------------------

# NAV History
if file.name == "02_nav_history.csv":

    # Sort by fund and date
    df = df.sort_values(["amfi_code", "date"])

    # Forward fill missing NAV values
    df["nav"] = (
        df.groupby("amfi_code")["nav"]
          .ffill()
    )

    # Remove invalid NAV
    df = df[df["nav"] > 0]


# Investor Transactions
if file.name == "08_investor_transactions.csv":

    df = df[df["amount_inr"] > 0]


# Scheme Performance
if file.name == "07_scheme_performance.csv":

    df = df[
        (df["expense_ratio_pct"] >= 0.1) &
        (df["expense_ratio_pct"] <= 2.5)
    ]


# Fund Master
if file.name == "01_fund_master.csv":

    df = df.drop_duplicates(subset=["amfi_code"])

    # ---------------------------
    # Save cleaned dataset
    # ---------------------------

    output_file = PROCESSED / ("clean_" + file.name)

    df.to_csv(output_file, index=False)

    # ---------------------------
    # Summary
    # ---------------------------

    summary.append({
        "Dataset": file.name,
        "Rows Before": rows_before,
        "Rows After": len(df),
        "Columns": len(df.columns),
        "Duplicates Removed": duplicate_rows,
        "Missing Values Remaining": int(df.isnull().sum().sum())
    })

    print(f"Rows Before : {rows_before}")
    print(f"Rows After  : {len(df)}")
    print(f"Duplicates Removed : {duplicate_rows}")
    print(f"Missing Values Remaining : {df.isnull().sum().sum()}")

# ==========================================================
# Cleaning Report
# ==========================================================

summary_df = pd.DataFrame(summary)

print("\n" + "=" * 70)
print("DATA CLEANING SUMMARY")
print("=" * 70)

print(summary_df)

summary_df.to_csv(
    REPORTS / "cleaning_report.csv",
    index=False
)

print("\nCleaning report saved successfully.")
print("Location :", REPORTS / "cleaning_report.csv")

print("\nAll datasets cleaned successfully!")