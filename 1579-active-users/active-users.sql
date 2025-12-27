with dedup as (
    select distinct id, login_date
    from Logins 
)

, agg as (
    select id, login_date, count(*) over (partition by id order by login_date
                                range between interval '4days' preceding and current row) as number 
    from dedup
)
select distinct a.id, a.name
from agg 
inner join Accounts a 
    on agg.id = a.id
where agg.number >= 5 
order by id

