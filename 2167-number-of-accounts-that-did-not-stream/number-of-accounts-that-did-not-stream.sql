select count(distinct account_id) as accounts_count
from Subscriptions sb 
where sb.start_date < '2022-01-01' and sb.end_date >= '2021-01-01'
    and not exists (select 1 from Streams s where s.account_id = sb.account_id and date_trunc('year', stream_date)::date = '2021-01-01')