-- Write your PostgreSQL query statement below

select
        Least(from_id, to_id) as person1,
        Greatest(from_id, to_id) as person2,
        count(*) as call_count,
        sum(duration) as total_duration 
from Calls
group by 1, 2 