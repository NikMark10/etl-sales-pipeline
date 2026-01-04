CREATE TABLE sales (
    order_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    order_date TIMESTAMP,
    amount NUMERIC,
    currency VARCHAR,
    country VARCHAR
);