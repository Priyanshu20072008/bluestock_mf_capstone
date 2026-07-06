from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

RAW_DATA = BASE_DIR / "data" / "raw"
PROCESSED_DATA = BASE_DIR / "data" / "processed"
DATABASE = BASE_DIR / "data" / "db" / "bluestock_mf.db"

LOGS = BASE_DIR / "logs"