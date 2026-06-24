"""
preprocess.py
Reusable preprocessing functions for the RetainIQ pipeline.
These functions are used by both the notebooks and the FastAPI app.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def fix_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    """
    TotalCharges comes in as object dtype in the raw dataset.
    Convert to numeric and handle any empty string edge cases.
    """
    # TODO: Implement this function
    # Hint: pd.to_numeric(df['TotalCharges'], errors='coerce')
    raise NotImplementedError("Implement fix_total_charges")


def encode_binary_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode all Yes/No binary columns to 1/0.
    """
    # TODO: Implement this function
    # Hint: map({'Yes': 1, 'No': 0}) for each binary column
    raise NotImplementedError("Implement encode_binary_columns")


def encode_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Label encode multi-class categorical columns.
    Returns the encoded dataframe and a dict of fitted encoders.
    """
    # TODO: Implement this function
    # Return: df, encoders_dict
    raise NotImplementedError("Implement encode_categorical_columns")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create derived features from existing columns.
    """
    # TODO: Implement at least 2 derived features
    # Ideas:
    #   df['avg_monthly_spend'] = df['TotalCharges'] / (df['tenure'] + 1)
    #   df['is_long_term'] = (df['tenure'] > 24).astype(int)
    raise NotImplementedError("Implement engineer_features")


def get_feature_columns() -> list:
    """
    Returns the list of feature column names used for prediction.
    Keep this in sync with what the model was trained on.
    """
    # TODO: Fill this in after notebook 02 is complete
    return []
