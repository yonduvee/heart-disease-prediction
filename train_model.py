from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "heart.csv"
MODEL_DIR = ROOT / "model"
MODEL_PATH = MODEL_DIR / "heart_model.joblib"

FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal",
]

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}\n"
            "Download heart.csv from Kaggle and put it in the data folder."
        )

    df = pd.read_csv(DATA_PATH)
    if "target" not in df.columns:
        raise ValueError("Expected a 'target' column in heart.csv.")
    missing = [column for column in FEATURES if column not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")

    df = df[FEATURES + ["target"]].dropna()
    X = df[FEATURES]
    y = df["target"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
    ])
    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.3f}")
    print(classification_report(y_test, predictions))

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump({
        "model": pipeline,
        "model_type": "Logistic Regression with StandardScaler",
        "features": FEATURES,
    }, MODEL_PATH)
    print(f"Saved model to: {MODEL_PATH}")

if __name__ == "__main__":
    main()
