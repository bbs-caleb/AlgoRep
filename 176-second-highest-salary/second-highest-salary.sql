SELECT (
    SELECT salary
    FROM (
        SELECT 
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
        FROM Employee
    ) AS ranked_salaries
    WHERE rnk = 2
    LIMIT 1 -- Ensures a single value is returned
) AS SecondHighestSalary;