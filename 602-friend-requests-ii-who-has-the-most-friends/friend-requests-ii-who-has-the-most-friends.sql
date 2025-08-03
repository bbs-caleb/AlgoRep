with how_many as (
    select 
        id1,
        count(distinct id2) as total
    from (
        select 
                requester_id as id1,
                accepter_id as id2
        from RequestAccepted

        union all

        select 
                accepter_id as id1,
                requester_id as id2
        from RequestAccepted
    )
    group by 1
    order by total DESC 
    limit 1
)
select id1 as id, total as num
from how_many