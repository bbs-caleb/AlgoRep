with first_year as (
    select
        product_id,
        min(year) as first_year
    from Sales 
    group by 1 )

select
        f.product_id, 
        f.first_year,
        s.quantity,
        s.price
from first_year f
join Sales s on f.product_id = s.product_id and f.first_year = s.year
