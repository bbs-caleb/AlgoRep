 with user_min_time as (
    select player_id, min(event_date) as min_dt
    from Activity
    group by player_id
 )

select u.player_id, a.device_id 
from user_min_time u 
inner join Activity a 
    on u.player_id = a.player_id and u.min_dt = a.event_date
    