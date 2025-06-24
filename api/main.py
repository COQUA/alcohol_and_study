from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib, numpy as np

app = FastAPI(title="Alcohol Study Predictor")

origins = ["http://127.0.0.1:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    raise RuntimeError("model.pkl no encontrado en la raíz del proyecto")

class InputData(BaseModel):
    Dalc: int; Walc: int; studytime: int; absences: int
    failures: int; goout: int; health: int; age: int
    sex: int; subject: int

@app.post("/predict")
def predict(data: InputData):
    x = np.array([[
      data.Dalc, data.Walc, data.studytime, data.absences,
      data.failures, data.goout, data.health,
      data.age, data.sex, data.subject
    ]])
    try:
        pred = model.predict(x)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"predicted_G3": round(float(pred), 2)}