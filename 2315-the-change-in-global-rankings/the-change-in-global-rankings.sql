with cte as (
    select 
        tp.team_id,
        tp.name,
        tp.points,
        coalesce(pc.points_change, 0) as points_change,
        rank() over (order by tp.points desc, tp.name) as prev_rank,
        rank() over (order by tp.points + coalesce(pc.points_change, 0) desc, tp.name) as current_rank
    from TeamPoints tp
    left join PointsChange pc
        on tp.team_id = pc.team_id  
)
select team_id, name, prev_rank - current_rank  as rank_diff
from cte 
order by team_id