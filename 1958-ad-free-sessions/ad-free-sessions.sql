select distinct session_id
from Playback p 
where not exists (select 1 from Ads a where a.customer_id = p.customer_id and a.timestamp between p.start_time and p.end_time)
order by session_id