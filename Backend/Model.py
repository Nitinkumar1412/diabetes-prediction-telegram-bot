import pickle
import pandas as pd
import numpy as np
#open the model file and load the model
with open('predictionModel.pkl', 'rb') as f:
    model = pickle.load(f)
    
def predict(data):
    try:
        input_df = pd.DataFrame([{
            'Pregnancies': data.pregnancies,
            'Glucose': data.Glucose,
            'BloodPressure': data.Blood_pressure,
            'SkinThickness': data.SkinThickness,
            'Insulin': data.insulin,
            'BMI': data.BMI,
            'Age': data.age
        }])

        result = model.predict(input_df)[0]

        if result == 1:
            return "High risk of diabetes"
        else:
            return "Low risk of diabetes"

    except Exception as ex:
        return f"Error: {str(ex)}"
    
    
    