"""
predict.py
Prediction logic used by the FastAPI app.
Loads the trained model and returns churn probability.
"""

import joblib
import numpy as np
import pandas as pd
from pathlib import Path

# Model path — relative to project root
MODEL_PATH = Path(__file__).parent / "model.pkl"


def load_model():
    """
    Load the trained sklearn model from disk.
    Raises FileNotFoundError if model.pkl doesn't exist yet.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}. "
            "Run notebook 03_modeling.ipynb first to train and save the model."
        )
    return joblib.load(MODEL_PATH)


def predict_churn(customer_data: dict) -> dict:
    """
    Takes a dict of customer features, returns churn probability and risk label.

    Args:
        customer_data: dict matching the schema in api/schemas.py

    Returns:
        dict with keys: churn_probability (float), risk_label (str)
    """
    # TODO: Implement this after model training is complete
    # Steps:
    # 1. Load model
    # 2. Convert customer_data to a DataFrame row
    # 3. Apply same preprocessing as notebook 02 (use preprocess.py functions)
    # 4. model.predict_proba() → get probability of class 1
    # 5. Return probability + risk label (High/Medium/Low based on thresholds)
    raise NotImplementedError("Implement after completing notebook 03")
