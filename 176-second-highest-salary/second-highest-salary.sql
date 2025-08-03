with 
    salary_ranks as (
        select 
                id,
                salary,
                dense_rank() over (order by salary DESC) as rk
        from    Employee
    )

    select null as SecondHighestSalary

    union all

    select salary 
    from salary_ranks 
    where rk = 2 

    order by SecondHighestSalary ASC  
    limit 1

    