select 
    customer_number
from Orders 
group by 1
order by count(*) desc 
limit 1 