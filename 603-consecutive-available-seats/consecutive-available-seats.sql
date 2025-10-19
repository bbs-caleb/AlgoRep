with cte as (
    select  seat_id, 
            free, 
            lag(free) over (order by seat_id) as prev_free,
            lead(free) over (order by seat_id) as next_free 
    from Cinema 
)

select seat_id 
from cte
where free = 1 and prev_free = 1 or free = 1 and next_free = 1