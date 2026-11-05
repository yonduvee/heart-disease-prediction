from pydantic import BaseModel, Field

class HeartDiseaseInput(BaseModel):
    age: int = Field(..., ge=1, le=120, example=52)
    sex: int = Field(..., ge=0, le=1, example=1)
    cp: int = Field(..., ge=0, le=3, example=0)
    trestbps: float = Field(..., gt=0, example=125)
    chol: float = Field(..., ge=0, example=212)
    fbs: int = Field(..., ge=0, le=1, example=0)
    restecg: int = Field(..., ge=0, le=2, example=1)
    thalach: float = Field(..., gt=0, example=168)
    exang: int = Field(..., ge=0, le=1, example=0)
    oldpeak: float = Field(..., ge=0, example=1.0)
    slope: int = Field(..., ge=0, le=2, example=2)
    ca: int = Field(..., ge=0, le=4, example=2)
    thal: int = Field(..., ge=0, le=3, example=2)
