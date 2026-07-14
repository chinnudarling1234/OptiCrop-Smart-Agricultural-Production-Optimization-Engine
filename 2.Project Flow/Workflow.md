# Workflow

---

## Project Overview

**OptiCrop** is a Smart Agricultural Production Optimization Engine that uses machine learning to recommend the best crops based on soil nutrients and environmental conditions.

## End-to-End Project Flow

```mermaid
flowchart TD
    A[1. Pre-requisites] --> B[2. Define Problem & Requirements]
    B --> C[3. Entity Relationship Diagram]
    C --> D[4. Data Collection & EDA]
    D --> E[5. Data Pre-processing]
    E --> F[6. Model Building]
    F --> G[7. Application Building]
    G --> H[8. Conclusion]

    D --> D1[Download Dataset]
    D --> D2[Univariate Analysis]
    D --> D3[Bivariate Analysis]
    D --> D4[Multivariate Analysis]

    E --> E1[Null Value Check]
    E --> E2[Outlier Handling]
    E --> E3[Seasonal Crop Extraction]
    E --> E4[Train-Test Split]

    F --> F1[K-Means Clustering]
    F --> F2[Logistic Regression]
    F --> F3[Model Evaluation]
    F --> F4[Crop Prediction]

    G --> G1[HTML Pages]
    G --> G2[Python Backend]
    G --> G3[Run Application]
```

## Application Scenarios

| Scenario | User | Flow |
|----------|------|------|
| **Scenario 1** | Farmer | Enter soil/climate data → ML recommends best crop |
| **Scenario 2** | Farmer | Select a crop → System assesses suitability score |
| **Scenario 3** | Researcher / Policy maker | Explore analytics, NPK patterns, sustainability insights |

## ML Pipeline Flow

```
Raw CSV Data
    ↓
Load & Clean (nulls, outliers)
    ↓
Exploratory Data Analysis (uni/bi/multivariate)
    ↓
Feature Scaling (StandardScaler)
    ↓
Train-Test Split (80/20)
    ↓
Model Comparison (KNN, LR, DT, RF, K-Means)
    ↓
Select Best Model → Save .pkl artifacts
    ↓
Flask API serves predictions via web UI
```

## Web Application Pages

| Page | Route | Purpose |
|------|-------|---------|
| Home | `/` | Landing page |
| Dashboard | `/dashboard` | Stats overview |
| Crop Recommendation | `/recommend` | Scenario 1 |
| Suitability Check | `/suitability` | Scenario 2 |
| Crop Catalog | `/crops` | Browse 22 crops |
| Seasonal Crops | `/seasonal` | Kharif / Rabi / Zaid crops |
| Research Hub | `/research` | Scenario 3 analytics |
| About | `/about` | Project info |
| How It Works | `/how-it-works` | ML pipeline explanation |

## Execution Order

1. Complete pre-requisites and install dependencies
2. Review business problem and ERD
3. Run Epic 2 analysis scripts (folder `5.Epic 2 - Data Collection and Analysis/`)
4. Run Epic 3 preprocessing scripts (folder `6.Epic 3 - Data Pre-processing/`)
5. Train models: `python train_model.py`
6. Launch app: `python app.py` → open `http://localhost:5000`
