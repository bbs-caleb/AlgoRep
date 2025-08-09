select sum(b.apple_count) + sum(coalesce(c.apple_count, 0)) as apple_count,
        sum(b.orange_count) + sum(coalesce(c.orange_count, 0)) as orange_count
from Boxes b 
left join Chests c on b.chest_id = c.chest_id 