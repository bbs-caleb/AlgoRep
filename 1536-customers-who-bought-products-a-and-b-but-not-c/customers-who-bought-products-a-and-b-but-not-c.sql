with cte as (
    select customer_id
    from Orders 
    group by customer_id 
    having sum(case when product_name = 'A' then 1 else 0 end) > 0 
            and sum(case when product_name = 'B' then 1 else 0 end) > 0
                and sum(case when product_name = 'C' then 1 else 0 end) = 0
)

select 
    c2.customer_id, 
    c2.customer_name
from cte c1
inner join Customers c2
    on c1.customer_id = c2.customer_id
order by customer_id