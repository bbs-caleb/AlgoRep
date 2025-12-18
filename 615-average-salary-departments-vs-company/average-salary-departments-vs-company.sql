with cte as (
    select 
            to_char(s.pay_date, 'YYYY-MM') as pay_month,
            e.department_id, 
            avg(s.amount) as avg_salary
    from Salary s 
    inner join Employee e 
        on s.employee_id = e.employee_id
    group by 1, 2
)

    , cte_2 as (
        select 
                to_char(s.pay_date, 'YYYY-MM') as pay_month,
                avg(s.amount) as avg_salary
        from Salary s 
        inner join Employee e 
            on s.employee_id = e.employee_id
        group by 1
    )

    select
            cte.pay_month,
            cte.department_id,
            case 
                when cte.avg_salary > cte_2.avg_salary
                        then 'higher'
                when cte.avg_salary < cte_2.avg_salary 
                        then 'lower'
                else 'same'
            end as comparison
    from cte 
    inner join cte_2
        on cte.pay_month = cte_2.pay_month;