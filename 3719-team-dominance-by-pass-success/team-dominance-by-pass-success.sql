-- Write your PostgreSQL query statement below
with cte as (
select 
    pass_from, 
    t1.team_name as team_name_from, 
    p.time_stamp, 
    p.pass_to, 
    t2.team_name as team_name_to,
    CASE
        WHEN (split_part(p.time_stamp, ':', 1)::int * 60
            + split_part(p.time_stamp, ':', 2)::int) <= 45*60
        THEN 1
        ELSE 2
      END AS half_number
from Passes p
join Teams t1 on p.pass_from = t1.player_id 
join Teams t2 on p.pass_to = t2.player_id ) 


select
    team_name_from as team_name,
    half_number,
    sum(case when team_name_from = team_name_to then 1 else -1 end)::integer as dominance
from cte
group by 1, 2
order by team_name, half_number 