-- =========================================
-- analysis_queries.sql
-- Analytical SQL for core KPIs
-- =========================================
-- 5 practical queries for retail banking analytics
-- =========================================

-- 1) Monthly Income and Expenses Summary
-- Calculates total income, expenses, and net balance per month
SELECT
    DATE_TRUNC('month', txn_date)::DATE AS month,
    SUM(CASE WHEN txn_type = 'Credit' THEN amount ELSE 0 END) AS total_income,
    SUM(CASE WHEN txn_type = 'Debit' THEN amount ELSE 0 END) AS total_expenses,
    SUM(CASE WHEN txn_type = 'Credit' THEN amount ELSE -amount END) AS net_balance
FROM transactions
GROUP BY 1
ORDER BY 1;

-- 2) Top 5 Customers by Transaction Volume
-- Identifies the most active customers by total transaction amount
SELECT
    c.customer_name,
    ROUND(SUM(ABS(t.amount)), 2) AS total_transaction_volume
FROM transactions t
JOIN accounts a ON a.account_id = t.account_id
JOIN customers c ON c.customer_id = a.customer_id
GROUP BY c.customer_name
ORDER BY total_transaction_volume DESC
LIMIT 5;

-- 3️) Average Spending by Category
-- Finds the average amount per expense transaction
SELECT
    category,
    ROUND(AVG(amount), 2) AS avg_spending
FROM transactions
WHERE txn_type = 'Debit'
GROUP BY category
ORDER BY avg_spending DESC;

-- 4) Running Balance per Account
-- Calculates cumulative balance per account in time order
SELECT
    a.account_id,
    txn_date,
    SUM(CASE WHEN txn_type = 'Credit' THEN amount ELSE -amount END)
        OVER (PARTITION BY a.account_id ORDER BY txn_date) AS running_balance
FROM transactions t
JOIN accounts a ON a.account_id = t.account_id
ORDER BY a.account_id, txn_date;

-- 5) New Customers per Month
-- Counts how many new customers joined each month
SELECT
    DATE_TRUNC('month', join_date)::DATE AS join_month,
    COUNT(*) AS new_customers
FROM customers
GROUP BY 1
ORDER BY 1;
