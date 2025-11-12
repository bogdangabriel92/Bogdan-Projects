-- export_results.sql
-- Exporta rezultatele analizelor in fisiere CSV in folderul /results

-- 1) KPI Monthly Summary
COPY (
  SELECT
    date_trunc('month', txn_date)::DATE AS month,
    SUM(CASE WHEN lower(txn_type) = 'credit' THEN amount ELSE 0 END) AS total_income,
    SUM(CASE WHEN lower(txn_type) = 'debit' THEN amount ELSE 0 END) AS total_expenses,
    SUM(CASE WHEN lower(txn_type) = 'credit' THEN amount ELSE -amount END) AS net_balance
  FROM transactions
  GROUP BY 1
  ORDER BY 1
) TO 'results/kpi_monthly_summary.csv' WITH (HEADER, DELIMITER ',');

-- 2) Top 5 Customers by Transaction Volume
COPY (
  SELECT
    c.customer_name,
    ROUND(SUM(ABS(t.amount)), 2) AS total_transaction_volume
  FROM transactions t
  JOIN accounts a ON a.account_id = t.account_id
  JOIN customers c ON c.customer_id = a.customer_id
  GROUP BY c.customer_name
  ORDER BY total_transaction_volume DESC
  LIMIT 5
) TO 'results/top_customers.csv' WITH (HEADER, DELIMITER ',');
