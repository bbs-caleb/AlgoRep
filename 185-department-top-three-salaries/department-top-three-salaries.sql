with ranks_salaries as (
    select 
            id, name, salary, departmentId, 
            dense_rank() over (partition by departmentId order by salary desc) as rk 
    from    Employee 
)

select
    d.name as Department,
    r.name as Employee,
    r.salary as Salary 
from ranks_salaries r
join Department d on r.departmentId = d.id 
where rk <= 3 
order by rk 