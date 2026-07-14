"""Checking for Null Values — Epic 3: Data Pre-processing
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from utils.data_loader import FEATURE_COLUMNS, load_dataset

print("=" * 60)
print("Checking for Null Values")
print("=" * 60)

df = load_dataset()

print("\nNull count per column:")
null_counts = df.isnull().sum()
for col, count in null_counts.items():
    status = "OK" if count == 0 else "NEEDS HANDLING"
    print(f"  {col:15s} nulls={count:5d}  [{status}]")

print(f"\nTotal null values: {df.isnull().sum().sum()}")
print(f"Total rows: {len(df)}")

# Check for empty strings in label
empty_labels = (df["label"].astype(str).str.strip() == "").sum()
print(f"Empty labels: {empty_labels}")

# After cleaning pipeline
from utils.preprocessing import clean_dataset

cleaned = clean_dataset(df)
print(f"\nAfter clean_dataset():")
print(f"  Rows before: {len(df)}")
print(f"  Rows after:  {len(cleaned)}")
print(f"  Rows removed: {len(df) - len(cleaned)}")
print(f"  Remaining nulls: {cleaned.isnull().sum().sum()}")
