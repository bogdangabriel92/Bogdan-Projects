SELECT
  CAST(order_date AS DATE) AS day,
  COUNT(DISTINCT order_id) AS orders,
  SUM(revenue) AS revenue,
  AVG(revenue) AS aov
FROM orders
GROUP BY CAST(order_date AS DATE)
ORDER BY day;