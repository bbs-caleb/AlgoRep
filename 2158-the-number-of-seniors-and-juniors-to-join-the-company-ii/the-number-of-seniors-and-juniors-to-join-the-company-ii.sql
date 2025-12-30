with cte as (
    select employee_id, experience, salary, sum(salary) over (partition by experience order by salary) as cummulative
    from Candidates  
)
, hired_seniors as (
    select *
    from cte 
    where cummulative <= 70000 and experience = 'Senior'
)
, left_ as (
    select 70000 - coalesce(max(cummulative), 0) as remaining_budget
    from hired_seniors 
)
, juniors as (
    select * 
    from cte c
    inner join left_ l 
        on c.cummulative <= l.remaining_budget and c.experience = 'Junior'
    where c.cummulative <= l.remaining_budget
)
select distinct employee_id 
from juniors

union

select distinct employee_id 
from hired_seniors 
