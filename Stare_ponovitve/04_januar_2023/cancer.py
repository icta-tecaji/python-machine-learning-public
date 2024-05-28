# Local imports
import datetime

# Third party imports
from pydantic import BaseModel, Field
from fastapi import FastAPI
import joblib
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Load model
model = joblib.load('data/model_binary.dat.gz')

model_name = "Breast Cancer Wisconsin (Diagnostic)"
version = "v1.0.0"

def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction


def get_model_response(input):
    X = pd.json_normalize(input.__dict__)
    prediction = predict(X, model)
    if prediction == 1:
        label = "M"
    else:
        label = "B"
    return {
        'label': label,
        'prediction': int(prediction)
    }

# Input for data validation
class Input(BaseModel):
    concavity_mean: float = Field(..., gt=0)
    concave_points_mean: float = Field(..., gt=0)
    perimeter_se: float = Field(..., gt=0)
    area_se: float = Field(..., gt=0)
    texture_worst: float = Field(..., gt=0)
    area_worst: float = Field(..., gt=0)

    class Config:
        schema_extra = {
            "concavity_mean": 0.3001,
            "concave_points_mean": 0.1471,
            "perimeter_se": 8.589,
            "area_se": 153.4,
            "texture_worst": 17.33,
            "area_worst": 2019.0,
        }


# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction: int


@app.get('/')
async def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name,
        "version": version
    }


@app.get('/health')
async def service_health():
    """Return service health"""
    return {
        "ok"
    }


@app.post('/predict', response_model=Output)
async def model_predict(input: Input):
    """Predict with input"""
    response = get_model_response(input)
    return response
