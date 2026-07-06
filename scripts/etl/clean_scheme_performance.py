"""
Clean scheme_performance.csv
Bluestock Mutual Fund Analytics
"""

from pathlib import Path
import pandas as pd

# -------------------------------------------------
# Paths
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

RAW = BASE_DIR / "data" / "raw"
PROCESSED = BASE_DIR / "data" / "processed"

INPUT_FILE = RAW / "07_scheme_performance.csv"
OUTPUT_FILE = PROCESSED / "clean_07_scheme_performance.csv"

print("=" * 70)
print("Cleaning Scheme Performance Dataset")
print("=" * 70)

# -------------------------------------------------
# Load Data
# -------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print(f"Rows Loaded : {len(df)}")

# -------------------------------------------------
# Numeric Validation
# -------------------------------------------------

numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -------------------------------------------------
# Check Missing Numeric Values
# -------------------------------------------------

missing_numeric = df[numeric_columns].isnull().sum().sum()

print(f"Missing Numeric Values : {missing_numeric}")

# -------------------------------------------------
# Expense Ratio Validation
# -------------------------------------------------

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(f"Invalid Expense Ratio : {len(invalid_expense)}")

# -------------------------------------------------
# Flag Return Anomalies
# -------------------------------------------------

anomalies = df[
    (df["return_1yr_pct"] < -100) |
    (df["return_3yr_pct"] < -100) |
    (df["return_5yr_pct"] < -100)
]

print(f"Return Anomalies : {len(anomalies)}")

# -------------------------------------------------
# Remove Duplicates
# -------------------------------------------------

duplicates = df.duplicated().sum()

print(f"Duplicate Rows : {duplicates}")

df = df.drop_duplicates()

# -------------------------------------------------
# Missing Values
# -------------------------------------------------

print("\nMissing Values")

print(df.isnull().sum())

# -------------------------------------------------
# Save
# -------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nCleaning Completed Successfully.")

print(f"Rows Saved : {len(df)}")
print(f"Output : {OUTPUT_FILE}")