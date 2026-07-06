"""
Clean investor_transactions.csv
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

INPUT_FILE = RAW / "08_investor_transactions.csv"
OUTPUT_FILE = PROCESSED / "clean_08_investor_transactions.csv"

print("=" * 70)
print("Cleaning Investor Transactions Dataset")
print("=" * 70)

# -------------------------------------------------
# Load Data
# -------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print(f"Rows Loaded : {len(df)}")

# -------------------------------------------------
# Convert Date
# -------------------------------------------------

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# -------------------------------------------------
# Standardize Transaction Types
# -------------------------------------------------

df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_transactions = ["Sip", "Lumpsum", "Redemption"]

invalid_transactions = df[
    ~df["transaction_type"].isin(valid_transactions)
]

print(f"Invalid Transaction Types : {len(invalid_transactions)}")

# -------------------------------------------------
# Validate Amount
# -------------------------------------------------

invalid_amount = df[df["amount_inr"] <= 0]

print(f"Invalid Amount Rows : {len(invalid_amount)}")

df = df[df["amount_inr"] > 0]

# -------------------------------------------------
# Validate KYC Status
# -------------------------------------------------

df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print(f"Invalid KYC Status : {len(invalid_kyc)}")

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
# Save Clean File
# -------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nCleaning Completed Successfully.")

print(f"Rows Saved : {len(df)}")
print(f"Output : {OUTPUT_FILE}")