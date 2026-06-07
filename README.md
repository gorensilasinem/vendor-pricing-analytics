# Vendor Pricing Intelligence Dashboard

An end-to-end data pipeline simulating a vendor pricing analytics system for a global food delivery platform operating across 65+ countries.

## Business Context
This project addresses a core challenge in food delivery platforms: **how to monitor and optimize vendor pricing strategies at scale** to improve affordability for millions of customers while supporting revenue growth for 1M+ restaurant partners.

## Tech Stack
| Layer | Tool |
|---|---|
| Data Generation | Python |
| Data Warehouse | DuckDB |
| Data Transformation | dbt Core |
| Orchestration | Apache Airflow |
| Visualization | Looker Studio |
| Version Control | Git |

## Pipeline Architecture

Raw Data (Python) --> DuckDB --> dbt (Staging + Marts) --> Looker Studio Dashboard
                                        ^
                                 Airflow DAG (Daily Schedule)

## dbt Models
- stg_vendors: cleaned vendor master data
- stg_orders: cleaned and filtered order transactions
- vendor_performance: aggregated vendor metrics with affordability segmentation and performance tiers

## Key Metrics
- 50,000 order transactions across 1,000 vendors
- 7 countries, 8 cuisine types
- Affordability scoring per vendor
- Performance tier classification (Top / Mid / Low Performer)

## Dashboard
<img width="825" height="617" alt="Ekran Resmi 2026-06-07 19 33 06" src="https://github.com/user-attachments/assets/4f7aa88f-fa94-4984-b785-5ddcb38ec9e0" />

Built in Looker Studio with 4 views:
- Revenue by Country
- Order Distribution by Cuisine Type
- Vendor Performance Tier
- Affordability Segment Analysis

## How to Run
1. python -m venv venv && source venv/bin/activate
2. pip install duckdb dbt-duckdb apache-airflow pandas
3. python data/raw/generate_data.py
4. python data/load_to_duckdb.py
5. cd vendor_pricing_dbt && dbt run

## Dashboard Preview
[View Live Dashboard](https://datastudio.google.com/reporting/56c70f5b-e94e-4c7a-8d5b-4fc9f67f09cb)

[Download Dashboard PDF](Vendor_Pricing_Intelligence_Dashboard.pdf)
