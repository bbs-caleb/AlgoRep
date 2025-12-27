with activity_agg as (
    select activity, count(distinct id) as total 
    from Friends 
    group by 1
)
, agg as (
    select max(total) as max_total, min(total) as min_total
    from activity_agg 
)
select activity 
from activity_agg ag 
where not exists (select 1 from agg a where a.max_total = ag.total or a.min_total = ag.total)
