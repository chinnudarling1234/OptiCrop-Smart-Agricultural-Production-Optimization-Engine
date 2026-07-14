"""Evaluating Model Performance and Saving the Best Model — Epic 4: Model Building
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from utils.model_trainer import (
    build_crop_profiles,
    compare_models,
    evaluate_kmeans_clustering,
    save_artifacts,
)
from utils.preprocessing import clean_dataset, encode_labels, scale_features
from utils.data_loader import FEATURE_COLUMNS

print("=" * 60)
print("Evaluating Model Performance and Saving the Best Model")
print("=" * 60)

summary, best_model, scaler, label_encoder, df = compare_models()
crop_profiles = build_crop_profiles(df)

X_scaled, _ = scale_features(df[FEATURE_COLUMNS], fit=True)
y_encoded, _ = encode_labels(df["label"])
kmeans_result = evaluate_kmeans_clustering(
    X_scaled, y_encoded, n_clusters=len(label_encoder.classes_)
)

save_artifacts(
    model=best_model,
    scaler=scaler,
    label_encoder=label_encoder,
    crop_profiles=crop_profiles,
    comparison_summary=summary,
    kmeans_model=kmeans_result["estimator"],
)

print(f"\nBest model: {summary['best_model']}")
print(f"Best accuracy: {summary['best_accuracy']:.4f}")
print("\nModel Comparison:")
for name, metrics in summary["comparison"].items():
    line = f"  {name:22s} accuracy={metrics['accuracy']:.4f}  cv={metrics['cv_mean']:.4f}±{metrics['cv_std']:.4f}"
    if "note" in metrics:
        line += f"  ({metrics['note']})"
    print(line)

print(f"\nK-Means silhouette: {summary['kmeans']['silhouette_score']:.4f}")
print(f"\nArtifacts saved to: {ROOT / 'models'}/")
print("  crop_model.pkl, scaler.pkl, label_encoder.pkl, crop_profiles.pkl, model_comparison.pkl, kmeans_model.pkl")
