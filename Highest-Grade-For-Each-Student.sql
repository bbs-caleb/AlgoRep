1with cte as (
2    select  student_id,
3            course_id,
4            grade,
5            row_number() over (partition by student_id 
6                        order by grade desc, course_id) as rnk
7    from Enrollments
8)
9
10select student_id, course_id, grade 
11from cte 
12where rnk = 1
13order by student_id