select e1.employee_id
from Employees e1 
where not exists (select 1 from Employees e2 where e1.manager_id = e2.employee_id)
    and e1.salary < 30000
and manager_id is not null
group by 1 
order by e1.employee_id 