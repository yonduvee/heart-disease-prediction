from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from app.schemas import HeartDiseaseInput

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "heart_model.joblib"

app = FastAPI(
    title="Heart Disease Prediction API",
    description="A demonstration API that predicts the presence of heart disease.",
    version="1.0.0",
)

model_bundle = None

@app.on_event("startup")
def load_model():
    global model_bundle
    if not MODEL_PATH.exists():
        raise RuntimeError(
            f"Model not found at {MODEL_PATH}. Run: python train_model.py"
        )
    model_bundle = joblib.load(MODEL_PATH)

@app.get("/")
def root():
    return {"message": "Heart Disease Prediction API. Visit /docs for Swagger UI."}

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model_bundle is not None}

@app.get("/info")
def info():
    if model_bundle is None:
        raise HTTPException(status_code=503, detail="Model is not loaded")
    return {
        "model_type": model_bundle["model_type"],
        "features": model_bundle["features"],
        "target": "heart disease presence (1) or absence (0)",
    }

@app.post("/predict")
def predict(data: HeartDiseaseInput):
    if model_bundle is None:
        raise HTTPException(status_code=503, detail="Model is not loaded")

    features = model_bundle["features"]
    input_data = pd.DataFrame([data.model_dump()])[features]
    prediction = int(model_bundle["model"].predict(input_data)[0])

    return {
        "heart_disease": bool(prediction),
        "prediction": prediction,
        "message": (
            "Prediction: heart disease present"
            if prediction == 1
            else "Prediction: heart disease absent"
        ),
        "disclaimer": "For educational use only; not a medical diagnosis.",
    }
