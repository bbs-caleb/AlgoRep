with ranks as  (
    select
        player_id,
        event_date,
        row_number() over (partition by player_id order by event_date) as rk 
    from    Activity
)

, first_ as (
    select *
    from ranks 
    where rk = 1 
)

, second_ as (
    select * 
    from ranks
    where rk = 2 
)

select      
        round(count(s.event_date)::numeric / count(*), 2) as fraction
from        first_ f
left join   second_ s on f.player_id = s.player_id and f.event_date + interval '1 day' = s.event_date
