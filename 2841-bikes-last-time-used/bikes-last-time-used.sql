select 
    bike_number,
    max(end_time) as end_time
from Bikes
group by 1 
order by end_time DESC