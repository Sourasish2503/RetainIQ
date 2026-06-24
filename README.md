# RetainIQ 🔍

> End-to-end Customer Churn Prediction & Analytics Platform

## Overview

RetainIQ predicts which customers are likely to churn using a full production-grade data stack — from raw data ingestion to a live REST API and a business intelligence dashboard.

**Built to demonstrate:** Python · SQL (Window Functions, CTEs) · BigQuery · dbt · FastAPI · scikit-learn · Power BI · GitHub

---

## Architecture

```
Raw CSV (Kaggle)
     │
     ▼
BigQuery (raw_customers)
     │
     ▼
dbt Pipeline
  ├── stg_customers          (staging — clean types & names)
  ├── int_engagement_metrics (intermediate — RFM window functions)
  └── fct_churn_features     (mart — final ML-ready feature table)
     │
     ▼
Python ML Pipeline (sklearn)
  ├── EDA & Preprocessing
  ├── Logistic Regression Model
  └── model.pkl (saved artifact)
     │
     ▼
FastAPI  ──────────────────────► POST /predict → churn probability
     │
     ▼
Power BI Dashboard
  ├── Churn Rate KPI
  ├── Churn by Contract Type
  ├── Revenue at Risk
  └── Top High-Risk Customers
```

---

## Project Structure

```
RetainIQ/
├── data/raw/                  # Raw dataset (not pushed to GitHub)
├── notebooks/                 # EDA, preprocessing, modeling notebooks
├── src/                       # Reusable Python modules
├── api/                       # FastAPI app
├── retainiq_dbt/              # dbt project
└── dashboard/screenshots/     # Power BI dashboard screenshots
```

---

## Setup

### 1. Clone & Install
```bash
git clone https://github.com/Sourasish2503/RetainIQ.git
cd RetainIQ
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file in the root:
```
GCP_PROJECT_ID=your-project-id
GCP_DATASET_ID=retainiq_raw
GCP_TABLE_ID=raw_customers
GOOGLE_APPLICATION_CREDENTIALS=gcp_keys.json
```

### 3. Run the API
```bash
uvicorn api.main:app --reload
```
API docs available at `http://localhost:8000/docs`

---

## Dataset
[Telco Customer Churn — Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## Dashboard
*(Screenshots will be added in Phase 6)*

---

## Results
*(Model metrics will be added after Phase 4)*

| Metric | Score |
|--------|-------|
| ROC-AUC | TBD |
| Accuracy | TBD |
| Precision | TBD |
| Recall | TBD |

---

*Built as a capstone portfolio project — Sourasish Bhattacharya*
