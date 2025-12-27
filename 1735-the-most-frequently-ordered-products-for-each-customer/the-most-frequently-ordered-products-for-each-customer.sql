with most_frequent as (
    select customer_id, product_id, count(*) as total 
    from Orders 
    group by 1, 2
)

, ranks as (
    select customer_id, product_id, dense_rank() over (partition by customer_id order by total desc) as rnk 
    from most_frequent
)

select 
        r.customer_id,
        r.product_id,
        p.product_name
from ranks r  
inner join Products p
    on p.product_id = r.product_id 
where r.rnk = 1 
