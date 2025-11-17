select 
    u.user_id,
    u.name, 
    coalesce(sum(r.distance), 0) as "traveled distance"
from Users u 
left join Rides r 
    on u.user_id = r.user_id 
group by 1, 2
order by u.user_id;