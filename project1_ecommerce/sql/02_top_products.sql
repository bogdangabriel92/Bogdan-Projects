SELECT
  p.category,
  p.product_id,
  SUM(oi.quantity) AS qty_sold,
  SUM(oi.quantity * oi.unit_price) AS sales
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
GROUP BY p.category, p.product_id
ORDER BY sales DESC
LIMIT 20;