with cte as (
select  country, 
        gold_medals, 
        silver_medals, 
        bronze_medals,
        row_number() over (order by 
                                gold_medals desc, 
                                silver_medals desc,
                                bronze_medals desc,
                                country) as rnk 
from Olympic)

select country, gold_medals, silver_medals, bronze_medals
from cte 
order by rnk;

