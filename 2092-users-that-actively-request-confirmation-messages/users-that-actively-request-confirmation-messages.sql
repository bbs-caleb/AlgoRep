

select distinct c1.user_id  
from Confirmations c1 
inner join Confirmations c2 
    on c1.user_id = c2.user_id
        and c1.time_stamp < c2.time_stamp 
        and c1.time_stamp + interval '24hours' >= c2.time_stamp
