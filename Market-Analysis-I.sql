-- Write your PostgreSQL query statement below

with orders_2019 as (
  select buyer_id, count(*) as cnt
  from orders
  where order_date >= date '2019-01-01'
    and order_date <  date '2020-01-01'
  group by buyer_id
)
select
  u.user_id as buyer_id,
  u.join_date,
  coalesce(o2019.cnt, 0) as orders_in_2019
from users u
left join orders_2019 o2019
  on o2019.buyer_id = u.user_id
order by u.user_id
