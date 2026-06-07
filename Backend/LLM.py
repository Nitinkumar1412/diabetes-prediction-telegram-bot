import os
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

def generateExplaination(data,result):
    
    prompt = f"""
        you are a medical assistant explaining diabetes prediction results.
            
        Model Prediction: {result}
            
        Patient Details:
        - Age: {data.age} years
        - Pregnancies: {data.pregnancies}
        - Glucose Level: {data.Glucose} mg/dL
        - Blood Pressure: {data.Blood_pressure} mmHg
        - Skin Thickness: {data.SkinThickness} mm
        - Insulin Level: {data.insulin} mIU/L
        - BMI: {data.BMI} kg/m²
        
        Provide a clear, concise explanation that includes:
        1. What this prediction means
        2. Key factors from the patient's data that influenced this result
        3. General advice about diabetes risk factors
        4. Recommendation to consult a healthcare professional
            
        Keep the explanation helpful and simple and sort and generate like a report
        """
    try:
        response = model.generate_content(prompt)
        explanation = response.text
    except Exception as llm_error:
        explanation = f"Model prediction: {result}"
        
    return {
        "prediction": result,
        "explanation": explanation
    }