with requests as (
    select sender_id, send_to_id
    from FriendRequest
    group by 1, 2 
)

    , accepted as (
        select requester_id, accepter_id
        from RequestAccepted
        group by 1, 2 
    )

select case when (select count(*) from requests) = 0 then 0.00
        else round((select count(*) from accepted) * 1.0 / (select count(*) from requests), 2)
        
        end as accept_rate