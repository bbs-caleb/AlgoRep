with cte as (
    select  player_id, 
            match_day, 
            result,
            lag(result) over (partition by player_id order by match_day) as prev_result
    from Matches 
)
, cte_2 as (
    select  player_id,
            match_day,
            result,
            case 
                when prev_result is null and result = 'Win' then 0
                when prev_result is null and result <> 'Win' then 1 
                when prev_result = 'Win' and result = 'Win' then 0 
                when prev_result <> 'Win' and result = 'Win' then 1 
                else 1
            end is_broke 
    from cte 
)
, cte_3 as (
    select  player_id,
            match_day,
            result,
            sum(is_broke) over (partition by player_id order by match_day) as grp
    from cte_2
)
, cte_4 as (
    select player_id, result, count(*) streak
    from cte_3
    group by player_id, result, grp
)
, cte_5 as (
    select player_id, max(streak) as longest_streak
    from cte_4
    where result = 'Win'
    group by 1
)
select 
    distinct m.player_id, coalesce(c.longest_streak, 0) as longest_streak
from Matches m
left join cte_5 c 
    on m.player_id = c.player_id
order by player_id