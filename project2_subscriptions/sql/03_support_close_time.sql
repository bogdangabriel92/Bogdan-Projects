SELECT
  DATE_TRUNC('month', opened_at) AS month,
  AVG(EXTRACT(EPOCH FROM (closed_at - opened_at)))/3600 AS avg_hours_to_close
FROM tickets
WHERE closed_at IS NOT NULL
GROUP BY 1
ORDER BY 1;