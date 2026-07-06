"""
Fetch live NAV data from mfapi.in
Author: Priyanshu
Project: Bluestock Mutual Fund Analytics
"""

import requests
import pandas as pd
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FOLDER = BASE_DIR / "data" / "raw"

# AMFI Scheme Codes
SCHEMES = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

def fetch_nav(scheme_name, scheme_code):
    """Fetch NAV history for one mutual fund."""

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nFetching {scheme_name}...")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = RAW_FOLDER / f"{scheme_name}_live_nav.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Saved: {filename.name}")
        print(f"Records: {len(nav_df)}")

    except Exception as e:
        print(f"Error fetching {scheme_name}")
        print(e)


def main():

    print("=" * 60)
    print("Bluestock Live NAV Fetch")
    print("=" * 60)

    for scheme, code in SCHEMES.items():
        fetch_nav(scheme, code)

    print("\nAll downloads completed.")


if __name__ == "__main__":
    main()