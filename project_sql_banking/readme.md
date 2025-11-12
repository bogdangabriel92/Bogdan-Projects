# Banking SQL Power BI Dashboard

This project simulates a simplified retail banking environment and demonstrates an end-to-end analytical workflow — from SQL-based data modeling to Power BI financial reporting.

**Objective:** Analyze monthly income, expenses, and net balance evolution, plus customer transaction volumes, and design an interactive dashboard suitable for corporate financial reporting.


## Project Structure

banking_sql_dashboard/
├─ data/
│ ├─ customers.csv
│ ├─ accounts.csv
│ └─ transactions.csv
├─ sql/
│ ├─ create_tables.sql
│ ├─ insert_sample_data.sql
│ ├─ analysis_queries.sql
│ └─ export_results.sql
├─ results/
│ ├─ kpi_monthly_summary.csv
│ └─ top_customers.csv
├─ powerbi/
│ └─ banking_dashboard.pbix
└─ README.md

## SQL Stage (Data Modeling)

### 1. `create_tables.sql`
Defines three core tables and primary/foreign keys:
- **customers** (customer_id, customer_name, city, join_date)
- **accounts** (account_id, customer_id, account_type, open_date)
- **transactions** (transaction_id, account_id, txn_date, amount, txn_type, category)

### 2. `insert_sample_data.sql`
Loads sample data into the three tables (from CSVs or inline INSERTs).

### 3. `analysis_queries.sql`
Computes the two analytical outputs used in the dashboard:
- **kpi_monthly_summary**: aggregated `total_income`, `total_expenses`, `net_balance` by `month`
- **top_customers**: top 5 customers by total transaction volume

### 4. `export_results.sql` 
Exports the two result sets to CSV so they can be consumed by reporting layers (Power BI / Excel). 

## How to Reproduce (No Server Required)

-> Python + DuckDB 

-> pip install duckdb pandas

-> Run a small Python runner that executes, in order:
create_tables.sql → insert_sample_data.sql → analysis_queries.sql → export_results.sql

-> The CSVs are generated under results/.

## Power BI Dashboard

- File: powerbi/banking_dashboard.pbix

- Page: Financial Overview

- KPIs (cards): Total Income, Total Expenses, Net Balance (color-coded)

- Profitability Indicator (KPI): [Net Balance] vs [Total Expenses] (Trend axis = month)

- Income vs Expenses (Clustered Column): Axis = month, Values = Total Income & Total Expenses

Net Balance Trend (Line): Axis = month, Values = Net Balance

Top 5 Customers (Bar): customer_name by total_transaction_volume

## Key Insights (example with sample data)

- Positive Net Balance across all months (stable profitability).

- Expenses remain significantly below Income (healthy cost control).

- Top customers contribute a large share of total transaction volume.

- Clear upward trend in Net Balance over time.

## Files

- data/: raw CSV inputs

- sql/: portable SQL logic (including export_results.sql)

- python/run_sql_analysis.py: automation runner (executes SQL pipeline with DuckDB)

- results/: analytical outputs (CSVs for reporting)

- powerbi/banking_dashboard.pbix: interactive dashboard

- README.md: documentation (this file)