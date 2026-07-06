"""
Create SQLite Database using schema.sql

Bluestock Mutual Fund Analytics
"""

from pathlib import Path
from sqlalchemy import create_engine, text

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DB_DIR = BASE_DIR / "data" / "db"
SQL_DIR = BASE_DIR / "sql"

DB_DIR.mkdir(exist_ok=True)

DATABASE = DB_DIR / "bluestock_mf.db"
SCHEMA = SQL_DIR / "schema.sql"

print("=" * 70)
print("Creating SQLite Database")
print("=" * 70)

# ==========================================================
# Create Engine
# ==========================================================

engine = create_engine(f"sqlite:///{DATABASE}")

# ==========================================================
# Read schema.sql
# ==========================================================

with open(SCHEMA, "r", encoding="utf-8") as file:
    schema = file.read()

# ==========================================================
# Execute schema
# ==========================================================

with engine.connect() as conn:

    for statement in schema.split(";"):

        statement = statement.strip()

        if statement:
            conn.execute(text(statement))

    conn.commit()

print("\nDatabase created successfully.")

print(f"\nLocation:\n{DATABASE}")