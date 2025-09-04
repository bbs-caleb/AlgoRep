select project_id
from (
    select  project_id,
            count(*) as cnt,
            rank() over (order by count(*) desc) as rnk
    from Project 
    group by 1
) t
where rnk = 1