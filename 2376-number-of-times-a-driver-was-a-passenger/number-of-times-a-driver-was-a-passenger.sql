with cte as (
select
    passenger_id as driver_id,
    count(*) as cnt 
from Rides r1 
where exists (select 1 from Rides r2 where r2.driver_id = r1.passenger_id)
group by 1)
select 
    distinct r.driver_id,
    coalesce(c.cnt, 0) as cnt 
from Rides r 
left join cte c 
    on r.driver_id = c.driver_id
order by cnt desc;
