with 
    cummulative as (
        select
                *,
                sum(weight) over (order by turn) as total
        from    Queue )
    
    , last_ as (
        select *
        from cummulative
        where total <= 1000
        order by turn DESC
        limit 1
    )

    select person_name
    from last_



