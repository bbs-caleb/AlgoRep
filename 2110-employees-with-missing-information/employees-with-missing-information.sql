# Write your MySQL query statement below
with cte as (

select employee_id 
from Employees 
union 
select employee_id
from Salaries)

select distinct cte.employee_id
from cte 
left join Employees e 
    on cte.employee_id = e.employee_id 
left join Salaries s 
    on cte.employee_id = s.employee_id
where e.employee_id is null or s.employee_id is null 
order by cte.employee_id


