with cte as (
    select order_id, product_id, order_date, dense_rank() over (partition by product_id order by order_date desc) as rnk 
    from Orders 
)
select p.product_name, p.product_id, cte.order_id, cte.order_date
from cte
inner join Products p 
    on cte.product_id = p.product_id
where rnk = 1
order by product_name, product_id, order_id