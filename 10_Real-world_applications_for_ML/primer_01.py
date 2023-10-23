from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load

app = FastAPI(title="Iris ML API", description="API for Iris ML model", version="0.1")
TARGETS = ['setosa', 'versicolor', 'virginica']


class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class IrisPredictedResponse(BaseModel):
    prediction: str
    probability: float


@app.on_event("startup")
async def load_model():
    global model
    model = load("data/iris_model.joblib")


@app.get("/api/status")
async def read_status():
    return {"status": "ok"}


@app.post("/api/iris/prediction", response_model=IrisPredictedResponse)
async def get_predictions(iris: Iris):
    data = np.array([iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]).reshape(1, -1)
    prediction = model.predict(data)
    probability = model.predict_proba(data)[0]
    return {"prediction": TARGETS[prediction[0]], "probability": probability[prediction[0]]}
