with cte as (
    select user_id, gender, row_number() over (partition by gender order by user_id) as rnk 
    from Genders
)
select user_id, gender
from cte 
order by rnk, case when gender = 'female' then 0
                   when gender = 'other' then 1 
                   when gender = 'male' then 2 end
