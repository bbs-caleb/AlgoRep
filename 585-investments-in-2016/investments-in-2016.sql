with repeated_2015 as (
    select tiv_2015
    from insurance
    group by tiv_2015
    having count(*) > 1
),

unique_locations as (
    select lat, lon
    from insurance
    group by lat, lon
    having count(*) = 1
)

select round(sum(i.tiv_2016)::numeric, 2) as tiv_2016
from insurance i
join repeated_2015 r
    on i.tiv_2015 = r.tiv_2015
join unique_locations u
    on i.lat = u.lat
   and i.lon = u.lon;
