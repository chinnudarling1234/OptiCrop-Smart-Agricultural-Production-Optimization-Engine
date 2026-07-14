# Run the Application

---

## Step-by-Step Instructions

### 1. Activate Virtual Environment

```bash
cd c:\Users\HP\Desktop\SIP
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Train the ML Model

```bash
python train_model.py
```

Expected output:
```
OptiCrop Model Training Complete
Best model: random_forest (accuracy: 0.99xx)
Artifacts saved to models/
```

### 3. Start the Flask Server

```bash
python app.py
```

Expected output:
```
 * Running on http://127.0.0.1:5000
```

### 4. Open in Browser

Navigate to: **http://localhost:5000**

---

## Pages to Test

| URL | Test Action |
|-----|-------------|
| http://localhost:5000/ | Verify landing page loads |
| http://localhost:5000/recommend | Submit NPK values, check crop result |
| http://localhost:5000/suitability | Select a crop, verify suitability score |
| http://localhost:5000/crops | Browse crop catalog |
| http://localhost:5000/seasonal | Filter by Kharif/Rabi/Zaid |
| http://localhost:5000/research | View analytics charts |
| http://localhost:5000/dashboard | Check dataset statistics |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError: crop_model.pkl` | Run `python train_model.py` first |
| Port 5000 in use | Set `FLASK_RUN_PORT=5001` or kill existing process |
| Module not found | Ensure venv is activated and `pip install -r requirements.txt` |
| Dataset missing | Place `Crop_recommendation.csv` in `data/` folder |

---

## Verification Checklist

- [ ] Model training completes without errors
- [ ] Flask server starts on port 5000
- [ ] Home page renders correctly
- [ ] Crop recommendation returns a result with confidence %
- [ ] Suitability check shows parameter breakdown
- [ ] Research page displays charts
- [ ] All API endpoints return valid JSON
