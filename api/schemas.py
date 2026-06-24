"""
schemas.py
Pydantic models for FastAPI request and response validation.
"""

from pydantic import BaseModel, Field
from typing import Literal


class CustomerInput(BaseModel):
    """
    Input schema — mirrors the features the model was trained on.
    TODO: Update field names and types after completing notebook 02.
    """
    tenure: int = Field(..., ge=0, le=72, description="Months as customer")
    monthly_charges: float = Field(..., gt=0, description="Monthly bill amount")
    total_charges: float = Field(..., ge=0, description="Total amount charged")
    contract: Literal["Month-to-month", "One year", "Two year"]
    internet_service: Literal["DSL", "Fiber optic", "No"]
    payment_method: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
    paperless_billing: Literal["Yes", "No"]
    tech_support: Literal["Yes", "No", "No internet service"]
    online_security: Literal["Yes", "No", "No internet service"]
    # TODO: Add remaining features after EDA confirms importance


class ChurnPrediction(BaseModel):
    """
    Response schema — what the API returns.
    """
    churn_probability: float = Field(..., description="Probability of churn (0.0 to 1.0)")
    risk_label: Literal["High", "Medium", "Low"] = Field(
        ..., description="Risk tier: High (>0.7), Medium (0.4-0.7), Low (<0.4)"
    )
    message: str


class HealthCheck(BaseModel):
    status: str
    model_loaded: bool
