# Heart Disease Prediction API

A learning project demonstrating a scikit-learn classifier served through FastAPI, packaged with Docker, and deployable to Render. This is not a medical device and must not be used for diagnosis or treatment decisions.

## Project structure

- `app/`: FastAPI application and Pydantic request schema
- `data/heart.csv`: Kaggle dataset (download separately; not committed)
- `model/heart_model.joblib`: trained model artifact (generated locally)
- `train_model.py`: trains and saves the model
- `Dockerfile`, `docker-compose.yml`: container setup

## 1. Download the dataset

Download the Heart Disease Dataset from:
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

Place the CSV named `heart.csv` in the `data/` directory. The training script expects the 13 feature columns in `train_model.py` and a binary `target` column.

## 2. Create a virtual environment and install packages

Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3. Train the model

```bash
python train_model.py
```

This creates `model/heart_model.joblib`. Keep this file in the repository because the Docker image copies it.

## 4. Run the API locally

```bash
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/info
- http://127.0.0.1:8000/docs

## 5. Build and run with Docker Compose

Make sure Docker Desktop is running, then:
```bash
docker compose build
docker compose up
```

Open http://localhost:8000/docs. Stop with `Ctrl+C`; optionally run `docker compose down`.

## 6. Test prediction

In Swagger UI, open `POST /predict`, click **Try it out**, and use this example:
```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 2,
  "thal": 2
}
```

The output includes `heart_disease` as a boolean. Predictions are illustrative only.

## 7. Deploy to Render

1. Push this project to a GitHub repository, including the trained `model/heart_model.joblib`.
2. In Render, choose **New + → Web Service** and connect the GitHub repository.
3. Select **Docker** as the runtime/environment and use the repository root as the Docker build context if the Dockerfile is at the root.
4. Create the service and wait for the image build and deployment.
5. Open the Render service URL and test `/health`, `/info`, and `/docs`.

The Docker command listens on Render's `PORT` environment variable (falling back to 8000 locally).

## Notes

- The model is intentionally simple; accuracy is not the focus of this assignment.
- The dataset and trained model are separate: train locally first, then commit the generated model artifact so Render can include it in the Docker image.
- Never commit credentials or API keys.
