with cte as (
    select distinct salary
    from Employee)

    , cte_2 as (
        select salary, row_number() over (order by salary desc) as rnk
        from cte 
    )

select salary as SecondHighestSalary
from cte_2
where rnk = 2 

union all

select Null 

order by SecondHighestSalary nulls last 
limit 1