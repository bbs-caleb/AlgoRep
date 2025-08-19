-- Write your PostgreSQL query statement below
select  gender,
        day,
        sum(score_points) over (
            partition by gender 
            order by day 
            range between unbounded preceding and current row
        ) as total 
from    Scores 
order by gender, day  