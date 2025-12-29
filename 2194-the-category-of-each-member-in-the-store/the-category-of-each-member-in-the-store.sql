with cte as (
    select 
        m.member_id, m.name,
        sum(case when v.visit_id is not null then 1 else 0 end) as total_visits,
        sum(case when p.visit_id is not null then 1 else 0 end) as total_purchases
    from Members m 
    left join Visits v 
        on m.member_id = v.member_id 
    left join Purchases p   
        on p.visit_id = v.visit_id 
    group by 1, 2
)
select member_id, name,
       case
            when total_visits = 0 then 'Bronze'
            when total_purchases::numeric / total_visits < 0.5 then 'Silver'
            when total_purchases::numeric / total_visits < 0.8 then 'Gold'
            when total_purchases::numeric / total_visits >= 0.8 then 'Diamond'
            else Null
        end as category
from cte 
