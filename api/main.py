"""
main.py
FastAPI application for RetainIQ churn prediction.

Endpoints:
  GET  /health  — health check, confirms model is loaded
  POST /predict — takes customer data, returns churn probability
"""

from fastapi import FastAPI, HTTPException
from api.schemas import CustomerInput, ChurnPrediction, HealthCheck

# TODO: Uncomment after implementing src/predict.py
# from src.predict import predict_churn, load_model

app = FastAPI(
    title="RetainIQ — Churn Prediction API",
    description="Predicts the probability of customer churn using a trained Logistic Regression model.",
    version="1.0.0"
)


@app.get("/health", response_model=HealthCheck, tags=["Health"])
def health_check():
    """
    Returns API status and whether the model is loaded.
    """
    # TODO: Try loading the model and return model_loaded=True if successful
    return HealthCheck(
        status="ok",
        model_loaded=False  # Change to True after model.pkl is ready
    )


@app.post("/predict", response_model=ChurnPrediction, tags=["Prediction"])
def predict(customer: CustomerInput):
    """
    Accepts customer data and returns churn probability.

    - **churn_probability**: Float between 0 and 1
    - **risk_label**: High / Medium / Low based on probability thresholds
    """
    # TODO: Implement after src/predict.py is complete
    # try:
    #     result = predict_churn(customer.model_dump())
    #     return ChurnPrediction(**result)
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))

    raise HTTPException(
        status_code=501,
        detail="Prediction endpoint not yet implemented. Complete notebooks 02 and 03 first."
    )
