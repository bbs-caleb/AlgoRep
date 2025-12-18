1with cte as (
2    select 
3            to_char(s.pay_date, 'YYYY-MM') as pay_month,
4            e.department_id, 
5            avg(s.amount) as avg_salary
6    from Salary s 
7    inner join Employee e 
8        on s.employee_id = e.employee_id
9    group by 1, 2
10)
11
12    , cte_2 as (
13        select 
14                to_char(s.pay_date, 'YYYY-MM') as pay_month,
15                avg(s.amount) as avg_salary
16        from Salary s 
17        inner join Employee e 
18            on s.employee_id = e.employee_id
19        group by 1
20    )
21
22    select
23            cte.pay_month,
24            cte.department_id,
25            case 
26                when cte.avg_salary > cte_2.avg_salary
27                        then 'higher'
28                when cte.avg_salary < cte_2.avg_salary 
29                        then 'lower'
30                else 'same'
31            end as comparison
32    from cte 
33    inner join cte_2
34        on cte.pay_month = cte_2.pay_month;