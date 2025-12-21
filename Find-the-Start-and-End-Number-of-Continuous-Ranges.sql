1with cte as (select log_id,
2                    lag(log_id) over (order by log_id) as prev_log_id
3             from Logs)
4   , cte_2 as (select log_id,
5                      prev_log_id,
6                      case
7                          when prev_log_id is not null and log_id - prev_log_id = 1 then 0
8                          else 1
9                          end as flg
10               from cte)
11   , cte_3 as (select log_id, prev_log_id, sum(flg) over (order by log_id) as grp
12               from cte_2)
13
14select min(log_id) as start_id, max(log_id) as end_id
15from cte_3
16group by grp
17order by start_id 