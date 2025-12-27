with cte as (
    select order_id, avg(quantity) as ord_avg, max(quantity) as ord_max
    from OrdersDetails 
    group by 1
)
select c1.order_id
from cte c1
where not exists (select 1 from cte c2 where c2.ord_avg >= c1.ord_max)
order by order_id