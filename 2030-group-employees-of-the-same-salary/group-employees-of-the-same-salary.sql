with cte as (
    select salary 
    from Employees 
    group by salary 
    having count(*) > 1
)
select 
    e.employee_id, e.name, e.salary, dense_rank() over (order by e.salary) as team_id
from Employees e 
inner join cte c 
    on e.salary = c.salary 
order by team_id, employee_id