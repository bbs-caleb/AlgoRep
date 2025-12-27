with cte as (
    select viewer_id, view_date, count(distinct article_id) as total 
    from Views 
    group by 1, 2
)
select distinct viewer_id as id 
from cte 
where total > 1
order by id 