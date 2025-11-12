-- =========================================
-- create_tables.sql
-- Banking SQL Basic Project
-- =========================================
-- Creates 3 core tables: customers, accounts, transactions
-- Each transaction links to an account, and each account links to a customer
-- =========================================

-- IMPORTANT: se sterg in ordinea corecta a dependentelor
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS customers;

-- Apoi se recreeaza
CREATE TABLE customers (
    customer_id   INTEGER PRIMARY KEY,
    customer_name VARCHAR,
    city          VARCHAR,
    join_date     DATE
);

CREATE TABLE accounts (
    account_id   INTEGER PRIMARY KEY,
    customer_id  INTEGER REFERENCES customers(customer_id),
    account_type VARCHAR,
    open_date    DATE
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id     INTEGER REFERENCES accounts(account_id),
    txn_date       DATE,
    amount         DECIMAL(10,2),
    txn_type       VARCHAR,
    category       VARCHAR
);

