-- Write your PostgreSQL query statement below
with cte as (
    select 
        transaction_id,
        day,
        sum(amount) as total 
    from Transactions
    group by 1, 2
)

    , daily_ranks as (
        select
            transaction_id,
            day,
            dense_rank() over (partition by day order by total DESC) as rk
        from cte 
    )

    select transaction_id 
    from daily_ranks 
    where rk = 1
    order by transaction_id 
