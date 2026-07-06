from pathlib import Path
import pandas as pd

# Get project root
BASE_DIR = Path(__file__).resolve().parents[2]

print("BASE_DIR:", BASE_DIR)

RAW_FOLDER = BASE_DIR / "data" / "raw"

print("RAW_FOLDER:", RAW_FOLDER)
print("Exists:", RAW_FOLDER.exists())

csv_files = list(RAW_FOLDER.glob("*.csv"))

print("CSV files found:", len(csv_files))

for f in csv_files:
    print(f.name)

print("=" * 70)
print("Bluestock Mutual Fund Data Ingestion")
print("=" * 70)

datasets = {}

summary = []

for file in csv_files:
    df = pd.read_csv(file)

    datasets[file.stem] = df

    rows, cols = df.shape
    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    summary.append({
        "Dataset": file.name,
        "Rows": rows,
        "Columns": cols,
        "Missing Values": missing,
        "Duplicate Rows": duplicates
    })

    print(f"\n{file.name}")
    print(f"Rows: {rows}")
    print(f"Columns: {cols}")
    print(f"Missing Values: {missing}")
    print(f"Duplicate Rows: {duplicates}")

summary_df = pd.DataFrame(summary)

print("\n========== DATA QUALITY REPORT ==========\n")
print(summary_df)

summary_df.to_csv(
    BASE_DIR / "reports" / "data_quality_report.csv",
    index=False
)

print(f"\nLoaded {len(datasets)} datasets successfully.")
print("Report saved successfully.")