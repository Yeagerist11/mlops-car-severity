
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Car Severity Prediction API")

MODEL_PATH = Path(__file__).parent / "models" / "car_severity_model.joblib"
model = joblib.load(MODEL_PATH)


class AccidentInput(BaseModel):
    impact_speed: float = Field(ge=0)
    damage_score: int = Field(ge=1, le=10)
    airbag_deployed: int = Field(ge=0, le=1)


@app.get("/")
def home():
    return {"message": "Car Severity Prediction API is running"}


@app.post("/predict")
def predict(accident: AccidentInput):
    data = pd.DataFrame([accident.model_dump()])
    prediction = model.predict(data)[0]

    return {"predicted_severity": str(prediction)}
