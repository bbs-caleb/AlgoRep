with cte as (
    select user1_id as a, user2_id as b
    from Friendship 

    union all 
    select user2_id, user1_id 
    from Friendship
)

select f.user1_id, f.user2_id, count(*) as common_friend
from Friendship f 
inner join cte c1
    on c1.a = f.user1_id 
inner join cte c2
    on f.user2_id = c2.a 
    and c1.b = c2.b
group by f.user1_id, f.user2_id
having count(*) >= 3
order by common_friend desc;