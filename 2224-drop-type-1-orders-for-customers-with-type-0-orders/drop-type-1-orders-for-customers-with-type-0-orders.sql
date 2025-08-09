with cte as (
    select  
            customer_id
    from Orders
    group by 1
    having sum(case when order_type = '0' then 1 else 0 end) > 0
)


select o.order_id, o.customer_id, o.order_type 
from    Orders o
left join cte c on o.customer_id = c.customer_id 
where (order_type = '1' and c.customer_id is null) or (order_type = '0' and c.customer_id is not null)
