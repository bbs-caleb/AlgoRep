with country_avg as (
    select country_id, avg(weather_state) as avg_
    from Weather
    where day >= '2019-11-01' and day < '2019-12-01'
    group by 1 
)

select c.country_name,
       case 
            when ca.avg_ <= 15 then 'Cold'
            when ca.avg_ >= 25 then 'Hot'
            else 'Warm'
        end as weather_type
from Countries c 
inner join country_avg ca 
    on c.country_id = ca.country_id
