with 
    daily_amount as (
        select 
            visited_on,
            sum(amount) as amount
        from Customer
        group by 1 )
    
    , cummulative_ as (
        select 
            visited_on,
            sum(amount) over (order by visited_on 
                        rows between 6 preceding
                        and current row) as amount,
            round(avg(amount) over (order by visited_on 
                        rows between 6 preceding
                        and current row), 2) as average_amount
        from daily_amount
    )


    select 
        visited_on,
        amount,
        average_amount
    from cummulative_ 
    where visited_on >= (
        select min(visited_on) + interval '6 days'
        from cummulative_
    )
    order by visited_on 