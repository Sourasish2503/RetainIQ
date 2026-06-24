# Dashboard

## Power BI Setup

1. Open Power BI Desktop
2. Get Data → Google BigQuery
3. Connect to your project and select `marts.fct_churn_features`
4. Build the following visuals:

### Required Visuals

| # | Visual Type | Fields | Purpose |
|---|-------------|--------|---------|
| 1 | **KPI Card** | `is_churned` (average) | Overall churn rate % |
| 2 | **Bar Chart** | `contract_type` vs `is_churned` | Churn by contract type |
| 3 | **Gauge** | `monthly_charges` × `is_churned` | Revenue at risk |
| 4 | **Table** | Top 20 customers by `contract_churn_rate` | High-risk customer list |
| 5 | **Donut Chart** | `risk_tier` | Distribution of risk tiers |

### Add screenshots here after completing the dashboard.
