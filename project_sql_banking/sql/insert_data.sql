-- =========================================
-- insert_sample_data.sql
-- Loads data from CSV files into base tables
-- =========================================
-- Adjust file paths based on your local environment
-- For SQL Server: use BULK INSERT instead of COPY
-- =========================================

-- Load data (PostgreSQL syntax)
COPY customers FROM 'data/customers.csv' DELIMITER ',' CSV HEADER;
COPY accounts FROM 'data/accounts.csv' DELIMITER ',' CSV HEADER;
COPY transactions FROM 'data/transactions.csv' DELIMITER ',' CSV HEADER;

-- Quick sanity checks
SELECT COUNT(*) AS total_customers FROM customers;
SELECT COUNT(*) AS total_accounts FROM accounts;
SELECT COUNT(*) AS total_transactions FROM transactions;

-- Preview first few records
SELECT * FROM transactions LIMIT 10;
