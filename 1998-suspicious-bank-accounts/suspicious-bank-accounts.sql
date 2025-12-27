with cte as (
    select 
        date_trunc('month', day)::date as month,
        account_id,
        sum(case when type = 'Creditor' then amount end) as total 
    from Transactions
    group by 1, 2
)

, cte_2 as (
    select 
        c.month,
        c.account_id,
        sum(case when c.total > a.max_income then 1 else 0 end) 
                over (partition by c.account_id order by c.month 
                        range between interval '1months' preceding and current row) as sum
    from cte c
    inner join Accounts a 
        on c.account_id = a.account_id
)
select distinct account_id
from cte_2
where sum = 2