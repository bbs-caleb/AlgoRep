SELECT
  CASE WHEN reqs.total_requests = 0 THEN 0.00
       ELSE ROUND(accs.total_accepts::numeric / reqs.total_requests, 2)
  END AS accept_rate
FROM
  (SELECT COUNT(DISTINCT (sender_id, send_to_id)) AS total_requests FROM FriendRequest) reqs,
  (SELECT COUNT(DISTINCT (requester_id, accepter_id)) AS total_accepts FROM RequestAccepted) accs;
