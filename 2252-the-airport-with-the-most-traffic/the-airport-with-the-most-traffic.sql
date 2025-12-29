with cte as (
    select departure_airport as a,
           arrival_airport as b,
           flights_count
    from Flights

    union all

    select arrival_airport as a,
           departure_airport as b,
           flights_count
    from Flights 
)
, cte_2 as (
    select a, sum(flights_count) as total
    from cte 
    group by 1 
)
, cte_3 as (
    select a, total, dense_rank() over (order by total desc) as rnk
    from cte_2
) 
select a as airport_id
from cte_3
where rnk = 1
order by airport_id