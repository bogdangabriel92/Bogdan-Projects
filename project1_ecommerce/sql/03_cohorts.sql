WITH first_order AS (
  SELECT customer_id, DATE_TRUNC('month', MIN(order_date)) AS cohort_month
  FROM orders
  GROUP BY customer_id
),
orders_m AS (
  SELECT customer_id, DATE_TRUNC('month', order_date) AS order_month
  FROM orders
)
SELECT
  f.cohort_month,
  o.order_month,
  COUNT(DISTINCT o.customer_id) AS active_customers,
  DATE_PART('month', AGE(o.order_month, f.cohort_month)) AS cohort_index
FROM first_order f
JOIN orders_m o USING (customer_id)
GROUP BY f.cohort_month, o.order_month, cohort_index
ORDER BY f.cohort_month, cohort_index;