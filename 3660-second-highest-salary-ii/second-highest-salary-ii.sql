with ranks_salary as (
    select 
        emp_id,
        salary,
        dept,
        dense_rank() over (partition by dept order by salary DESC) as rk 
    from employees

)


select 
    emp_id,
    dept
from ranks_salary
where rk = 2 
order by emp_id 