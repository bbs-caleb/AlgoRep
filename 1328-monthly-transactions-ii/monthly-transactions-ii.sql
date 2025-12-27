with full_rows as (
    select 
        to_char(trans_date, 'YYYY-MM') as month,
        country,
        count(*) filter (where state = 'approved') as approved_count,
        sum(amount) filter (where state = 'approved') as approved_amount,
        0 as chargeback_count,
        0 as chargeback_amount 
    from Transactions 
    group by 1, 2

    union all 

    select 
        to_char(cb.trans_date, 'YYYY-MM') as month,
        t.country,
        0 as approved_count,
        0 as approved_amount,
        count(t.amount) as chargeback_count,
        sum(t.amount) as chargeback_amount 
    from Transactions t  
    inner join Chargebacks cb 
        on t.id = cb.trans_id
    group by 1, 2
)
 
 , agg as (
    select 
        month,
        country,
        sum(approved_count) as approved_count,
        sum(approved_amount) as approved_amount,
        sum(chargeback_count) as chargeback_count,
        sum(chargeback_amount) as chargeback_amount
    from full_rows
    group by month, country
 )

 select * 
 from agg 
 where approved_count + approved_amount + chargeback_count + chargeback_amount > 0
