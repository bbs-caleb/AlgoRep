SELECT
  SUM(CASE WHEN EXTRACT(DOW FROM submit_date) IN (0, 6) THEN 1 ELSE 0 END) AS weekend_cnt, -- 0=Sunday, 6=Saturday
  SUM(CASE WHEN EXTRACT(DOW FROM submit_date) BETWEEN 1 AND 5 THEN 1 ELSE 0 END) AS working_cnt
FROM Tasks;
