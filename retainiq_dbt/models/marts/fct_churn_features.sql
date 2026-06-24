-- fct_churn_features.sql
-- Layer 3: Mart (Fact Table)
-- Purpose: Final ML-ready feature table. This is what Power BI connects to
--          and what gets exported for model training validation.

{{ config(materialized='table') }}

with enriched as (
    select * from {{ ref('int_engagement_metrics') }}
)

select
    -- IDs
    customer_id,

    -- Core features for ML
    tenure_months,
    monthly_charges,
    total_charges,
    avg_monthly_spend,
    charge_vs_avg,
    charge_percentile,
    service_count,
    is_monthly_contract,
    is_senior_citizen,

    -- Encoded contract type (for Power BI slicers)
    contract_type,
    internet_service,
    payment_method,
    tenure_segment,

    -- Group-level risk signals
    contract_churn_rate,
    internet_churn_rate,

    -- Target
    is_churned,

    -- Derived risk label for dashboard
    case
        when contract_churn_rate >= 0.4 and is_monthly_contract = 1 then 'High'
        when contract_churn_rate >= 0.2                             then 'Medium'
        else 'Low'
    end                                                             as risk_tier

from enriched
