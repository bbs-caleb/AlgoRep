with cte as (
    select 
            gs.day_, s.product_id, s.average_daily_sales 
    from Sales s 
    cross join lateral generate_series(s.period_start, s.period_end, interval '1d') gs(day_)
)
select 
    p.product_id, 
    p.product_name,
    to_char(c.day_, 'YYYY') as report_year,
    sum(average_daily_sales) as total_amount
from Product p 
inner join cte c 
    on p.product_id = c.product_id 
group by 1, 2, 3
order by product_id, report_year