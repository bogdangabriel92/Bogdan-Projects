# Project 2 – Subscription Churn & Support Analytics

## Obiectiv
Analiza unui business de tip SaaS/abonamente pentru a înțelege MRR, ARPU, churn și factori care influențează retenția.

## Structură
- `data_raw/` – CSV-uri brute (customers, subscriptions, usage, tickets, surveys)
- `sql/` – interogări SQL pentru MRR, ARPU, churn rate, support metrics
- `notebooks/` – Jupyter notebooks (churn analysis, vizualizări)
- `python/` – scripturi pentru extragerea churn flag și metrics
- `dashboard2.pbix` – Power BI Dashboard

## SQL scripts
- `01_mrr_arpu.sql` – calcule MRR și ARPU
- `02_active_customers.sql` – număr clienți activi
- `03_churn_rate.sql` – churn rate lunar
- `04_support_metrics.sql` – analiza ticketelor

## Python notebooks
- `churn_analysis.ipynb` – analiza churn (usage, tickets, churn flag, vizualizări cu Seaborn)

