from fastapi import FastAPI
from pydantic import BaseModel
from Model import predict
from LLM import generateExplaination
from pydantic import BaseModel,Field
from typing import Annotated
import pandas as pd


app = FastAPI()
# Request schema


class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    pregnancies: Annotated[int, Field(..., gt=0, description='Pregnancies of the user')]
    Glucose: Annotated[float, Field(..., gt=0, lt=200, description='Glucose level of the user')]
    Blood_pressure: Annotated[float, Field(..., gt=0, description='Blood pressure of the user')]
    SkinThickness: Annotated[float, Field(..., gt=0, description='skin thickness of the user')]
    insulin: Annotated[float, Field(..., gt=30,lt=230, description='Insulin of the user')]
    BMI: Annotated[float, Field(..., gt=0, description='BMI of the user')]


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def get_prediction(data: UserInput):
    
    # Convert to dict for ML model
    input_df = pd.DataFrame([{
        'age': data.age,
        'pregnancies': data.pregnancies,
        'Glucose': data.Glucose,
        'Blood_pressure': data.Blood_pressure,
        'SkinThickness': data.SkinThickness,
        'insulin': data.insulin,
        'BMI': data.BMI
    }])

    # ML prediction
    result = predict(input_df)
    

    # LLM explanation
    output = generateExplaination(data, result)

    return output