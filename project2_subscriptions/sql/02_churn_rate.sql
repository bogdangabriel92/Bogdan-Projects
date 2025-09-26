WITH active AS (
  SELECT DATE_TRUNC('month', period_start) AS month, customer_id
  FROM subscriptions
  WHERE is_active = TRUE
  GROUP BY 1, 2
),
roll AS (
  SELECT
    a.month,
    COUNT(DISTINCT a.customer_id) AS active_t,
    COUNT(DISTINCT b.customer_id) AS active_t1
  FROM active a
  LEFT JOIN active b
    ON b.customer_id = a.customer_id
   AND b.month = a.month + INTERVAL '1 month'
  GROUP BY a.month
)
SELECT
  month,
  active_t,
  active_t1,
  (active_t - active_t1)::float / active_t AS churn_rate
FROM roll
ORDER BY month;