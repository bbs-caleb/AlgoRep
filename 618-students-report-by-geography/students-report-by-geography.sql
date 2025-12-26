with cte as (
    select row_number() over (partition by continent order by name) as id, s.name, s.continent
    from Student s)

select 
    max(case when continent = 'America' then name end) as America,
    max(case when continent = 'Asia' then name end) as Asia, 
    max(case when continent = 'Europe' then name end) as Europe
from cte 
group by id
order by id
