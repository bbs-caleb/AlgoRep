with cte as (
    select  home_team_id as team_id, 
            count(*) as matches_played,
            sum(
                case 
                    when home_team_goals - away_team_goals > 0 then 3 
                    when home_team_goals - away_team_goals = 0 then 1
                    when home_team_goals - away_team_goals < 0 then 0
            end) as points,
            sum(home_team_goals) as goal_for,
            sum(away_team_goals) as goal_against,
            sum(home_team_goals - away_team_goals) as goal_diff
    from  Matches 
    group by home_team_id


    union all 

    select  away_team_id as team_id, 
            count(*) as matches_played,
            sum(
                case 
                    when home_team_goals - away_team_goals > 0 then 0 
                    when home_team_goals - away_team_goals = 0 then 1
                    when home_team_goals - away_team_goals < 0 then 3
            end) as points,
            sum(away_team_goals) as goal_for,
            sum(home_team_goals) as goal_against,
            sum(away_team_goals - home_team_goals) as goal_diff
    from  Matches 
    group by 1
)
, cte_2 as (
    select  team_id, 
            sum(matches_played) as mathes_played,
            sum(points) as points,
            sum(goal_for) as goal_for,
            sum(goal_against) as goal_against,
            sum(goal_diff) as goal_diff
    from cte c 
    group by 1
)
select 
        t.team_name,
        coalesce(c.mathes_played, 0) as matches_played,
        coalesce(c.points, 0) as points,
        coalesce(c.goal_for, 0) as goal_for,
        coalesce(c.goal_against, 0) as goal_against,
        coalesce(c.goal_diff, 0) as goal_diff
from Teams t 
inner join cte_2 c 
    on t.team_id = c.team_id
order by points desc, goal_diff desc, team_name