with cte as (
select 
        p.id, 
        p.name,
        cn.name as country, 
        c.duration,
        avg(duration) over () as total_avg,
        avg(duration) over (partition by cn.name) as country_avg
from Calls c 
inner join Person p
    on c.caller_id = p.id or c.callee_id = p.id
inner join Country cn
    on left(p.phone_number, 3) = cn.country_code)
select distinct country
from cte 
where country_avg > total_avg