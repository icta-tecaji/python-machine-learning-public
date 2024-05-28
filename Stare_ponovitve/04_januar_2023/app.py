from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel, conlist
from typing import List, Any

app = FastAPI(title="Iris ML API", description="API for iris dataset ml model", version="1.0")
model = None

@app.on_event('startup')
async def load_model():
    global model
    model = load('data/iris_dt_v1.joblib')

@app.get("/")
def read_root():
    return {"Hello": "World"}

class IrisPredictionResponse(BaseModel):
    prediction: List[int]
    probability: List[Any]
    log_probability: List[Any]


class Iris(BaseModel):
    data: List[conlist(float, min_items=4, max_items=4)]

@app.post('/iris/predict',
        tags=["Predictions"],
        response_model=IrisPredictionResponse,
        description="Get a classification from Iris")
async def get_prediction(iris: Iris):
    data = dict(iris)['data']
    prediction = model.predict(data).tolist()
    probability = model.predict_proba(data).tolist()
    log_probability = model.predict_log_proba(data).tolist()
    return {"prediction": prediction,
            "probability": probability,
            "log_probability": log_probability}



