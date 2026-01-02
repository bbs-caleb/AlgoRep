select 
    order_date,
    round(sum(case when customer_pref_delivery_date = order_date then 1 else 0 end)::numeric / count(*) * 100, 2) as immediate_percentage
from Delivery
group by 1 
order by order_date