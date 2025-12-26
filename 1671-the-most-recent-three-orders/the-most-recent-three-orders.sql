with cte as (
    select 
            c.customer_id, c.name, o.order_id, o.order_date,
            row_number() over (partition by c.customer_id order by o.order_date desc) as rnk
    from Customers c 
    inner join Orders o 
        on c.customer_id = o.customer_id
)
select name as customer_name, customer_id, order_id, order_date
from cte 
where rnk <= 3 
order by customer_name, customer_id, order_date desc;


