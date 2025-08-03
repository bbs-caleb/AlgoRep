select
        distinct num as ConsecutiveNums
from (
    select id, num, lead(num) over (order by id) num_1, lead(num, 2) over (order by id) num_2
    from Logs
)
where num  = num_1 and num_1 = num_2 