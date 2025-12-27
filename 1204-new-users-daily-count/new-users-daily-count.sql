with cte as (
    select user_id, activity, activity_date, row_number() over (partition by user_id order by activity_date) as rnk  
    from Traffic 
    where activity = 'login'
)
select activity_date as login_date, count(distinct user_id) as user_count 
from cte 
where rnk = 1 and activity_date >= '2019-06-30'::date - interval '90 days' and activity_date <= '2019-06-30'::date  
group by 1
order by login_date;
