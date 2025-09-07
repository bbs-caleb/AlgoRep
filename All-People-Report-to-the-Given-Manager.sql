with recursive chain as (
  select employee_id, manager_id, 0 as depth
  from employees
  where employee_id = 1

  union all

  select e.employee_id, e.manager_id, c.depth + 1
  from employees e
  join chain c on e.manager_id = c.employee_id
  where c.depth < 3
)
select distinct employee_id
from chain
where employee_id <> 1