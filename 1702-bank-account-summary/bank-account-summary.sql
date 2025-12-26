with cte as (
    select u.user_id, u.user_name, u.credit, t.trans_id, t.paid_by, t.paid_to, t.transacted_on,
            coalesce(
            case 
                when u.user_id = t.paid_by then amount 
                when u.user_id = t.paid_to then -amount 
            end, 0) as amount
    from Users u 
    left join Transactions t 
        on (u.user_id = t.paid_by or u.user_id = t.paid_to)
)

select 
        user_id, user_name, credit - credit_ as credit, 
                case 
                    when credit - credit_ < 0 then 'Yes'
                    else 'No'
                end as credit_limit_breached
from (
select user_id, user_name, credit, sum(amount) as credit_
from cte
group by 1, 2, 3)
order by user_id, user_name
