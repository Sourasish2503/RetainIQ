-- stg_customers.sql
-- Layer 1: Staging
-- Purpose: Clean raw column names, fix data types, remove duplicates.
-- Source: BigQuery raw_customers table (uploaded from telco_churn.csv)

{{ config(materialized='table') }}

with raw as (
    select *
    from `{{ var('project_id') }}.retainiq_raw.raw_customers`
),

cleaned as (
    select
        -- Customer identifier
        customerID                                          as customer_id,

        -- Demographics
        gender,
        SeniorCitizen                                       as is_senior_citizen,
        Partner,
        Dependents                                          as has_dependents,

        -- Account info
        cast(tenure as INT64)                              as tenure_months,
        Contract                                            as contract_type,
        PaperlessBilling                                   as paperless_billing,
        PaymentMethod                                      as payment_method,

        -- Charges — TotalCharges has edge case empty strings, handle safely
        cast(MonthlyCharges as FLOAT64)                    as monthly_charges,
        safe_cast(
            nullif(trim(TotalCharges), '') as FLOAT64
        )                                                  as total_charges,

        -- Services
        PhoneService                                        as phone_service,
        MultipleLines                                       as multiple_lines,
        InternetService                                     as internet_service,
        OnlineSecurity                                      as online_security,
        OnlineBackup                                        as online_backup,
        DeviceProtection                                    as device_protection,
        TechSupport                                         as tech_support,
        StreamingTV                                         as streaming_tv,
        StreamingMovies                                     as streaming_movies,

        -- Target variable
        case when Churn = 'Yes' then 1 else 0 end          as is_churned

    from raw
    -- Remove any duplicate customerIDs
    qualify row_number() over (partition by customerID order by customerID) = 1
)

select * from cleaned
