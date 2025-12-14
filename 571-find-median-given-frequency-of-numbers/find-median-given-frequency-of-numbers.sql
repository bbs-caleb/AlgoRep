WITH ordered AS (
  SELECT
    num,
    frequency,
    SUM(frequency) OVER (ORDER BY num) AS cum,
    SUM(frequency) OVER ()             AS total
  FROM Numbers
),
pos AS (
  SELECT DISTINCT
    (total + 1) / 2 AS p1,
    (total + 2) / 2 AS p2
  FROM ordered
),
hits AS (
  SELECT
    o.num,
    (o.cum - o.frequency + 1) AS lo,
    o.cum                      AS hi,
    p.p1, p.p2
  FROM ordered o
  CROSS JOIN pos p
)
SELECT ROUND(AVG(num)::numeric, 1) AS median
FROM (
  SELECT num FROM hits WHERE p1 BETWEEN lo AND hi
  UNION ALL
  SELECT num FROM hits WHERE p2 BETWEEN lo AND hi
) x;
