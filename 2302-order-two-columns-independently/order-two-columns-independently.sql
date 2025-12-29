with cte as (
    select  first_col, 
            second_col,
            row_number() over (order by first_col) as rnk1,
            row_number() over (order by second_col desc) as rnk2
    from Data 
)
select c1.first_col, c2.second_col
from cte c1 
inner join cte c2 
    on c1.rnk1 = c2.rnk2
order by c1.rnk1