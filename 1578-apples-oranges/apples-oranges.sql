select
    sale_date,
    sum(
        case
            when fruit = 'apples' then sold_num
            when fruit = 'oranges' then -sold_num
            else 0
        end
    ) as diff
from Sales
group by sale_date
order by sale_date;
