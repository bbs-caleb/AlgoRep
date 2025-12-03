SELECT
    company_id,
    employee_id,
    employee_name,
    ROUND(
        salary *
        (
            1 -
            CASE
                WHEN max_salary < 1000 THEN 0.0
                WHEN max_salary <= 10000 THEN 0.24
                ELSE 0.49
            END
        )
    ) AS salary
FROM (
    SELECT
        company_id,
        employee_id,
        employee_name,
        salary,
        MAX(salary) OVER (PARTITION BY company_id) AS max_salary
    FROM Salaries
) t;
