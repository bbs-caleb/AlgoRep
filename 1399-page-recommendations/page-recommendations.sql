with friends as (
    select user1_id as user_id 
    from Friendship 
    where user2_id = 1 

    union 

    select user2_id as user_id 
    from Friendship 
    where user1_id = 1 
)

, likes_ as (
    select distinct page_id as recommended_page 
    from Likes l
    inner join friends f 
        on l.user_id = f.user_id 
    where not exists (select 1 from Likes l2 where l2.page_id = l.page_id and l2.user_id = 1)
)

select *
from likes_