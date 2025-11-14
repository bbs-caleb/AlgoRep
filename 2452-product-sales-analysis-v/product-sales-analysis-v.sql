select  s.user_id, coalesce(sum(s.quantity * p.price), 0) as spending 
from Sales s 
left join Product p 
    on s.product_id = p.product_id
group by 1
order by spending desc, s.user_id