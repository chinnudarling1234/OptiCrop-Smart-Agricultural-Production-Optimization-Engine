"""Univariate Analysis — Epic 2: Data Collection and Analysis
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_loader import FEATURE_COLUMNS, load_dataset

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 60)
print("Univariate Analysis")
print("=" * 60)

df = load_dataset()
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(3, 3, figsize=(14, 12))
axes = axes.flatten()

for i, col in enumerate(FEATURE_COLUMNS):
    sns.histplot(df[col], kde=True, ax=axes[i], color="steelblue")
    axes[i].set_title(f"Distribution of {col}")
    axes[i].set_xlabel(col)

# Crop label distribution
sns.countplot(y=df["label"], order=df["label"].value_counts().index, ax=axes[7], palette="husl")
axes[7].set_title("Crop Label Distribution")
axes[8].axis("off")

plt.tight_layout()
chart_path = OUTPUT_DIR / "univariate_analysis.png"
plt.savefig(chart_path, dpi=120, bbox_inches="tight")
plt.close()

print(f"\nFeature statistics:")
for col in FEATURE_COLUMNS:
    print(f"  {col:12s} mean={df[col].mean():8.2f}  std={df[col].std():8.2f}  "
          f"min={df[col].min():8.2f}  max={df[col].max():8.2f}")

print(f"\nChart saved: {chart_path}")
