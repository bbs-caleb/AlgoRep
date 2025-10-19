SELECT DISTINCT ON (player_id) player_id, device_id
FROM Activity
ORDER BY player_id, event_date;
