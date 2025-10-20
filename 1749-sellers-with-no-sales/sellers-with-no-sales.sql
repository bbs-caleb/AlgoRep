select s.seller_name
from Seller s 
left join Orders o 
    on s.seller_id = o.seller_id
group by s.seller_name 
having count(o.order_id) filter (where o.sale_date >= '20200101' and o.sale_date < '20210101') = 0 
order by seller_name 