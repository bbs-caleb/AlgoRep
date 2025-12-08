
with cte as (
select  
        student_id,
        subject,
        first_value(score) over (
            partition by student_id, subject
            order by exam_date::date
            rows between unbounded preceding and unbounded following
        ) as first_score,
        last_value(score) over (
            partition by student_id, subject 
            order by exam_date::date
            rows between unbounded preceding and unbounded following
        ) as latest_score
from Scores ) 

select  student_id, 
        subject,
        first_score, 
        latest_score
from cte 
where first_score < latest_score
group by 1, 2, 3, 4
order by student_id, subject;