with cte as (
    select match_id, 'host' as status, host_team as team, host_goals as goals
    from Matches 

    union all

    select match_id, 'guest' as status, guest_team as team, guest_goals  as goals 
    from Matches 
)
, agg as (
    select match_id, sum(case when status = 'host' then goals else -goals end) as points
    from cte 
    group by 1 
)
select  c.team as team_id, 
        t.team_name,
        coalesce(sum(
        case 
            when c.status = 'host' and a.points > 0 then 3
            when c.status = 'host' and a.points = 0 then 1 
            when c.status = 'host' and a.points < 0 then 0
            when c.status = 'guest' and a.points < 0 then 3
            when c.status = 'guest' and a.points = 0 then 1 
            when c.status = 'guest' and a.points > 0 then 0
        end), 0) as  num_points
from cte c 
left join agg a 
    on c.match_id = a.match_id
inner join Teams t 
    on t.team_id = c.team
group by 1, 2

union all
select team_id, team_name, 0 as num_points
from Teams t
where not exists (select 1 from Matches m where t.team_id = m.host_team or t.team_id = m.guest_team)
order by num_points desc, team_id
