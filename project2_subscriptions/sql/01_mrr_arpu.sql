SELECT
  DATE_TRUNC('month', period_start) AS month,
  SUM(mrr) AS mrr,
  SUM(mrr) / NULLIF(COUNT(DISTINCT customer_id), 0) AS arpu
FROM subscriptions
WHERE is_active = TRUE
GROUP BY DATE_TRUNC('month', period_start)
ORDER BY month;