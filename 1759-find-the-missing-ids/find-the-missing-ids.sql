with cte as (
    select max(customer_id) as mx
    from Customers c 
)

, cte_2 as (
    select gs.ids
    from cte c 
    cross join lateral generate_series(1, c.mx) as gs(ids) 
)
select ids
from cte_2 c 
where not exists (select 1 from Customers cs where cs.customer_id = c.ids)
order by ids