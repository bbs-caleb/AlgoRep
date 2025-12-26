with cte as (
    select *, row_number() over (partition by username order by startDate desc) as rnk
    from UserActivity
)
, cte_2 as (
    select *, row_number() over (partition by username order by startDate) as rk 
    from cte 
    where rnk <= 2
)

select username, activity, startDate, endDate
from cte_2 
where rk = 1