-- int_engagement_metrics.sql
-- Layer 2: Intermediate
-- Purpose: Engineer RFM-style engagement features using SQL window functions.
--          This is the layer where advanced SQL (CTEs + window functions) lives.

{{ config(materialized='table') }}

with base as (
    select * from {{ ref('stg_customers') }}
),

-- RFM-style feature engineering in pure SQL
with_features as (
    select
        *,

        -- Recency proxy: customers with lower tenure are "newer" (higher churn risk)
        case
            when tenure_months <= 12  then 'New'
            when tenure_months <= 24  then 'Growing'
            when tenure_months <= 48  then 'Established'
            else 'Loyal'
        end                                                         as tenure_segment,

        -- Monetary: average spend per month
        safe_divide(total_charges, tenure_months)                   as avg_monthly_spend,

        -- Charge delta: how much more are they paying vs average customer?
        -- Window function: compare each customer to the overall average
        monthly_charges - avg(monthly_charges) over ()              as charge_vs_avg,

        -- Percentile rank of monthly charges (window function)
        percent_rank() over (order by monthly_charges)              as charge_percentile,

        -- Service count: how many services does the customer have?
        (
            case when phone_service     = 'Yes' then 1 else 0 end +
            case when online_security   = 'Yes' then 1 else 0 end +
            case when online_backup     = 'Yes' then 1 else 0 end +
            case when device_protection = 'Yes' then 1 else 0 end +
            case when tech_support      = 'Yes' then 1 else 0 end +
            case when streaming_tv      = 'Yes' then 1 else 0 end +
            case when streaming_movies  = 'Yes' then 1 else 0 end
        )                                                           as service_count,

        -- Contract risk flag
        case when contract_type = 'Month-to-month' then 1 else 0 end as is_monthly_contract,

        -- Churn rate by contract type (window function — group-level aggregation)
        avg(cast(is_churned as FLOAT64)) over (
            partition by contract_type
        )                                                           as contract_churn_rate,

        -- Churn rate by internet service type (window function)
        avg(cast(is_churned as FLOAT64)) over (
            partition by internet_service
        )                                                           as internet_churn_rate

    from base
)

select * from with_features
