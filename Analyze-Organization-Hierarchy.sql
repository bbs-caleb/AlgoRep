1with recursive
2    lvl as (select employee_id, 1 as level
3            from employees
4            where manager_id is null
5
6            union all
7
8            select e.employee_id, l.level + 1
9            from lvl l
10                     join employees e
11                          on e.manager_id = l.employee_id),
12    rel as (select employee_id as manager_id, employee_id as subordinate_id
13            from employees
14
15            union all
16
17            select r.manager_id, e.employee_id
18            from rel r
19                     join employees e
20                          on e.manager_id = r.subordinate_id),
21    agg as (select r.manager_id  as employee_id,
22                   count(*) - 1  as team_size,
23                   sum(e.salary) as budget
24            from rel r
25                     join employees e
26                          on e.employee_id = r.subordinate_id
27            group by r.manager_id)
28select e.employee_id,
29       e.employee_name,
30       l.level,
31       a.team_size,
32       a.budget
33from employees e
34         join lvl l
35              on l.employee_id = e.employee_id
36         join agg a
37              on a.employee_id = e.employee_id
38order by l.level asc,
39         a.budget desc,
40         e.employee_name asc