# Heart Disease Prediction API

A learning project demonstrating a scikit-learn classifier served through FastAPI, packaged with Docker, and deployed to Render.

This is not a medical device and must not be used for diagnosis or treatment decisions.

## Live Deployment

The Heart Disease Prediction API is successfully deployed on Render.

- **Live Application:** https://heart-disease-prediction-li67.onrender.com
- **Swagger UI Documentation:** https://heart-disease-prediction-li67.onrender.com/docs
- **Health Check:** https://heart-disease-prediction-li67.onrender.com/health
- **Model Information:** https://heart-disease-prediction-li67.onrender.com/info

**Deployment Status:** Live and successfully tested.

## Project Structure

```text
heart-disease-prediction/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── data/
│   └── heart.csv
│
├── model/
│   └── heart_model.joblib
│
├── train_model.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .gitignore
└── .dockerignore
```

- `app/`: FastAPI application and Pydantic request schema.
- `data/heart.csv`: Kaggle dataset (download separately; not committed).
- `model/heart_model.joblib`: Trained model artifact.
- `train_model.py`: Trains and saves the model.
- `Dockerfile`: Docker image configuration.
- `docker-compose.yml`: Docker Compose configuration.

## 1. Download the Dataset

Download the Heart Disease Dataset from Kaggle:

https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

Place the CSV named `heart.csv` inside the `data/` directory.

The training script expects 13 feature columns and a binary `target` column.

## 2. Create a Virtual Environment and Install Packages

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3. Train the Model

Run:

```bash
python train_model.py
```

This creates:

`model/heart_model.joblib`

The trained model artifact must be included in the GitHub repository because the Docker image copies it during the build.

## 4. Run the API Locally

Start FastAPI using Uvicorn:

```bash
uvicorn app.main:app --reload
```

Open the following endpoints:

- Health Check: http://127.0.0.1:8000/health
- Model Information: http://127.0.0.1:8000/info
- Swagger UI: http://127.0.0.1:8000/docs

## 5. Build and Run with Docker Compose

Make sure Docker Desktop is running.

Build the Docker image:

```bash
docker compose build
```

Start the container:

```bash
docker compose up
```

Open Swagger UI:

http://localhost:8000/docs

Stop the application using `Ctrl + C`.

Optionally remove the container and network:

```bash
docker compose down
```

## 6. Test Prediction

In Swagger UI:

1. Open the `POST /predict` endpoint.
2. Click **Try it out**.
3. Enter the following example JSON:

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

4. Click **Execute**.

The response includes `heart_disease` as a boolean and `prediction` as a binary value.

Example response:

```json
{
  "heart_disease": false,
  "prediction": 0,
  "message": "Prediction: heart disease absent",
  "disclaimer": "For educational use only; not a medical diagnosis."
}
```

Predictions are illustrative only and are not medical diagnoses.

## 7. Deploy to Render

1. Push the project to a GitHub repository, including the trained `model/heart_model.joblib` file.
2. In Render, select **New + → Web Service**.
3. Connect the GitHub repository.
4. Select **Docker** as the runtime/environment.
5. Use the repository root as the Docker build context.
6. Set the Dockerfile path to `Dockerfile`.
7. Create the service and wait for the Docker image build and deployment.
8. Test the deployed application using `/health`, `/info`, and `/docs`.

## 8. Technologies Used

- Python
- FastAPI
- Pydantic
- Scikit-learn
- Pandas
- Joblib
- Uvicorn
- Docker
- Docker Compose
- Git and GitHub
- Render

## 9. Notes and Disclaimer

- The model is intentionally simple; achieving high accuracy is not the focus of this assignment.
- The dataset and trained model are separate. Download the dataset and train locally first.
- The generated model artifact must be committed to GitHub so Render can include it in the Docker image.
- Never commit credentials, passwords, or API keys.
- This project is intended strictly for educational purposes.
- This application must not be used for medical diagnosis or treatment decisions.

---

**Project:** Heart Disease Prediction API  
**Deployment Platform:** Render  
**Repository:** https://github.com/yonduvee/heart-disease-prediction  
**Live Application:** https://heart-disease-prediction-li67.onrender.com
