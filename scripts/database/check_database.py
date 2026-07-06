"""
Verify SQLite Database
"""

from pathlib import Path
from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE = BASE_DIR / "data" / "db" / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DATABASE}")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

print("=" * 70)
print("DATABASE VERIFICATION")
print("=" * 70)

with engine.connect() as conn:

    for table in tables:

        result = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        )

        count = result.scalar()

        print(f"{table:<25} {count}")

print("\nDatabase verification completed successfully.")