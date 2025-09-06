-- Write your PostgreSQL query statement below
SELECT id, company, salary
FROM (
  SELECT
    id,
    company,
    salary,
    ROW_NUMBER() OVER (
      PARTITION BY company
      ORDER BY salary, id
    ) AS rn,
    COUNT(*) OVER (PARTITION BY company) AS n
  FROM Employee
) t
WHERE rn IN ( (n + 1) / 2, (n + 2) / 2 )
