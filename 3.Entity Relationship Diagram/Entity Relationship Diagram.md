# Entity Relationship Diagram

---

## OptiCrop — Entity Relationship Diagram

Logical data model for the Smart Agricultural Production Optimization Engine.

---

## Conceptual ERD

```mermaid
erDiagram
    ENVIRONMENTAL_CONDITION ||--o{ TRAINING_RECORD : "describes"
    CROP ||--o{ TRAINING_RECORD : "labels"
    CROP ||--o{ CROP_PROFILE : "has"
    ENVIRONMENTAL_CONDITION ||--o{ USER_INPUT : "captures"
    USER_INPUT ||--o| CROP_RECOMMENDATION : "generates"
    CROP_RECOMMENDATION ||--|{ RECOMMENDATION_ALTERNATIVE : "includes"
    CROP ||--o{ RECOMMENDATION_ALTERNATIVE : "ranked_as"
    CROP ||--o{ SUITABILITY_ASSESSMENT : "evaluates"
    USER_INPUT ||--o| SUITABILITY_ASSESSMENT : "triggers"
    SUITABILITY_ASSESSMENT ||--|{ PARAMETER_SCORE : "breaks_down"
    ML_MODEL ||--o{ CROP_RECOMMENDATION : "powers"
    ML_MODEL ||--o{ SUITABILITY_ASSESSMENT : "powers"
    CROP ||--o{ POLICY_INSIGHT_CROP : "referenced_in"
    POLICY_INSIGHT ||--|{ POLICY_INSIGHT_CROP : "lists"

    ENVIRONMENTAL_CONDITION {
        int condition_id PK
        float nitrogen_N
        float phosphorus_P
        float potassium_K
        float temperature
        float humidity
        float ph
        float rainfall
    }

    CROP {
        int crop_id PK
        string crop_name UK
        int sample_count
    }

    TRAINING_RECORD {
        int record_id PK
        int condition_id FK
        int crop_id FK
    }

    CROP_PROFILE {
        int profile_id PK
        int crop_id FK
        string parameter_name
        float mean_value
        float std_dev
        float min_value
        float max_value
    }

    USER_INPUT {
        int input_id PK
        string user_role
        datetime created_at
        int condition_id FK
    }

    CROP_RECOMMENDATION {
        int recommendation_id PK
        int input_id FK
        int recommended_crop_id FK
        float confidence_percent
    }

    ML_MODEL {
        int model_id PK
        string algorithm
        float accuracy
        string model_file
        string scaler_file
    }
```

---

## Entity Descriptions

| Entity | Description |
|--------|-------------|
| **ENVIRONMENTAL_CONDITION** | Soil NPK, pH, temperature, humidity, and rainfall values |
| **CROP** | One of 22 supported crop types (rice, maize, cotton, etc.) |
| **TRAINING_RECORD** | A labeled row from the 2,200-sample dataset |
| **CROP_PROFILE** | Statistical ranges (mean, min, max) per crop per parameter |
| **USER_INPUT** | Farmer, researcher, or policymaker field data submission |
| **CROP_RECOMMENDATION** | Scenario 1 output — best crop with confidence |
| **SUITABILITY_ASSESSMENT** | Scenario 2 output — compatibility report for a chosen crop |
| **ML_MODEL** | Trained classifier + StandardScaler saved as `.pkl` files |

---

## Mapping to Project Files

| ERD Entity | Implementation |
|------------|----------------|
| TRAINING_RECORD | `data/Crop_recommendation.csv` |
| CROP_PROFILE | `models/crop_profiles.pkl` |
| ML_MODEL | `models/crop_model.pkl`, `scaler.pkl`, `label_encoder.pkl` |
| USER_INPUT | Flask API request body (`/api/recommend`, `/api/suitability`) |
| CROP_RECOMMENDATION | `utils/model_service.recommend_crops()` |
| SUITABILITY_ASSESSMENT | `utils/model_service.assess_crop_suitability()` |
