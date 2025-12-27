with unique_spams as (
    select distinct post_id, action_date
    from Actions 
    where extra = 'spam'
)

, percents as (
    select u.action_date, sum(case when r.remove_date is not null then 1 else 0 end)::numeric / count(*) as percent 
    from unique_spams u 
    left join Removals r 
        on u.post_id = r.post_id 
    group by 1 
)

select round(avg(percent) * 100, 2) as average_daily_percent
from percents
