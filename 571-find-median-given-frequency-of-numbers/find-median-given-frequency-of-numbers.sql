with cte as (
    select  
            num, 
            row_number() over (order by num) as rnk,
            count(*) over () as total
    from numbers n
    cross join lateral generate_series(1, n.frequency) as gs(i)
)

select
        round(avg(num), 1) as median
from cte 
where 
    case 
        when total % 2 = 1 and total / 2 + 1 = rnk 
            then true
        when total % 2 = 0 and (rnk = total / 2 or rnk = total / 2 + 1)
            then true
        else false
    end
    