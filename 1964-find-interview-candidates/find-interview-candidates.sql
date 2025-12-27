with cte as (
    select contest_id, 'gold' as medal, gold_medal as user_id
    from Contests 

    union all

    select contest_id, 'silver' as medal, silver_medal as user_id
    from Contests 

    union all

    select contest_id, 'bronze' as medal, bronze_medal as user_id
    from Contests 
)

, cte_2 as (
select 
        medal, user_id, count(*) over (partition by user_id order by contest_id range between 2 preceding and current row) as total,
                sum(case when medal = 'gold' then 1 end) over (partition by user_id) as gold_medals 
from cte )
select distinct u.name, u.mail
from cte_2 
inner join Users u 
    on cte_2.user_id = u.user_id 
where total >= 3 or gold_medals >= 3
