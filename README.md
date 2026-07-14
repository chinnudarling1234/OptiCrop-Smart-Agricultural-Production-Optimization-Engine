# OptiCrop: Smart Agricultural Production Optimization Engine

An intelligent web application that uses machine learning to optimize agricultural production by analyzing soil nutrients (N, P, K), temperature, humidity, pH, and rainfall to recommend the best crops and assess suitability.

## Features

### Scenario 1: Smart Crop Recommendation
Farmers enter soil and environmental parameters. The ML engine recommends the most suitable crop for maximum yield.

### Scenario 2: Crop Suitability Assessment
Users select a specific crop and evaluate whether current conditions are compatible, with detailed parameter scoring and productivity insights.

### Scenario 3: Research & Policy Hub
Researchers and policymakers can explore crop-environment relationships, visual analytics, NPK demand patterns, and sustainability recommendations.

### Seasonal Crop Extraction
Browse crops by **Kharif**, **Rabi**, **Zaid**, and **Perennial** seasons. Infer the growing season from field conditions and get season-filtered ML recommendations.

## Tech Stack

- **Backend:** Flask (modular Python)
- **ML:** Scikit-learn — KNN, Logistic Regression, Decision Tree, Random Forest, K-Means
- **Data:** Pandas, NumPy
- **Analytics:** Matplotlib, Seaborn, SciPy
- **Frontend:** HTML, CSS, Bootstrap-style responsive layout, JavaScript
- **Persistence:** Pickle / Joblib (`.pkl`)

## Dataset

Uses the standard Crop Recommendation dataset (2,200 samples, 22 crops) with features:
- Nitrogen (N), Phosphorus (P), Potassium (K)
- Temperature, Humidity, pH, Rainfall
- Crop label

## HTML Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Landing page with project overview |
| Dashboard | `/dashboard` | Central hub for all tools |
| Crop Recommendation | `/recommend` | Scenario 1 — ML crop recommendation |
| Suitability Check | `/suitability` | Scenario 2 — Crop compatibility assessment |
| Crop Catalog | `/crops` | Browse all 22 crops with ideal ranges |
| Seasonal Crops | `/seasonal` | Extract crops by season + season-aware recommendations |
| Research Hub | `/research` | Scenario 3 — Analytics and policy insights |
| About | `/about` | Project vision and technology stack |
| How It Works | `/how-it-works` | ML pipeline explanation |

## Setup

```bash
# 1. Create virtual environment (Python 3.10+)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the ML model (compares KNN, LR, DT, RF, K-Means)
python train_model.py

# 4. Run the application
python app.py
```

Open **http://localhost:5000** in your browser.

## Project Structure

```
SIP/
├── app.py                      # Flask application
├── train_model.py              # Model training entry point
├── requirements.txt
├── data/
│   └── Crop_recommendation.csv
├── models/                     # Saved ML artifacts (generated)
│   ├── crop_model.pkl          # Best classifier
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│   ├── crop_profiles.pkl
│   ├── model_comparison.pkl    # Algorithm comparison metrics
│   └── kmeans_model.pkl        # K-Means clustering model
├── utils/
│   ├── data_loader.py          # Dataset loading
│   ├── preprocessing.py        # Cleaning, scaling, validation
│   ├── model_trainer.py        # Training & model comparison
│   ├── model_service.py        # Prediction & suitability
│   ├── seasonal_crops.py       # Seasonal crop extraction
│   └── analytics.py            # Research analytics
├── notebooks/
│   └── model_comparison.ipynb  # Jupyter EDA & training notebook
├── templates/                  # HTML templates
└── static/                     # CSS, JS, charts
```

## ML Pipeline

1. **Preprocess** — missing values, outlier trimming, label encoding, StandardScaler
2. **Compare** — KNN, Logistic Regression, Decision Tree, Random Forest (supervised); K-Means (unsupervised clustering)
3. **Select** — best supervised model by test accuracy
4. **Persist** — save `.pkl` artifacts for Flask inference

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/recommend` | POST | Get crop recommendations |
| `/api/suitability` | POST | Assess crop suitability |
| `/api/crops` | GET | List available crops |
| `/api/seasonal` | GET | List crops by season (`?season=kharif`) |
| `/api/seasonal/recommend` | POST | Season-inferred crop recommendations |
| `/api/seasonal/clusters` | GET | K-Means cluster analysis |
| `/api/research/summary` | GET | Research data summary |

### Example API Request (Recommendation)

```json
POST /api/recommend
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 21,
  "humidity": 82,
  "ph": 6.5,
  "rainfall": 203
}
```

### Example: Seasonal Crop Extraction

```json
GET /api/seasonal?season=kharif

POST /api/seasonal/recommend
{
  "N": 90, "P": 42, "K": 43,
  "temperature": 28, "humidity": 85,
  "ph": 6.5, "rainfall": 250
}
```

## License

Educational / Academic Project
