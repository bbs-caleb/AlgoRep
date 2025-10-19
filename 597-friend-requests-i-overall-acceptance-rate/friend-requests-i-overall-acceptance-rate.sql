WITH
UniqueAccepts AS (
    SELECT COUNT(DISTINCT (requester_id, accepter_id)) as num_accepts
    FROM RequestAccepted
),
UniqueRequests AS (
    SELECT COUNT(DISTINCT (sender_id, send_to_id)) as num_requests
    FROM FriendRequest
)
SELECT
    ROUND(
        COALESCE(
            ua.num_accepts::numeric / NULLIF(ur.num_requests, 0),
            0
        ),
        2
    ) AS accept_rate
FROM
    UniqueAccepts ua,
    UniqueRequests ur;