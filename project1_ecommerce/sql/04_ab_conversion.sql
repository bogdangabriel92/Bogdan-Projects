WITH conv AS (
  SELECT
    is_variant_B,
    COUNT(*) FILTER (WHERE converted = 1) AS conversions,
    COUNT(*)::float AS sessions
  FROM sessions
  GROUP BY is_variant_B
)
SELECT
  is_variant_B,
  conversions,
  sessions,
  conversions / sessions AS conversion_rate
FROM conv;