with cte as (
    select student_id, subject, min(exam_date) as first_date, max(exam_date) as last_date
    from Scores 
    group by 1, 2 
    having min(exam_date::date) != max(exam_date::date)
)

    , cte_2 as (
        select  s.student_id, 
                s.subject, 
                sum(case when s.exam_date = c.first_date then s.score else 0 end) as first_score, 
                sum(case when s.exam_date = c.last_date then s.score else 0 end) as latest_score
        from Scores s 
        inner join cte c 
            on s.student_id = c.student_id 
                and s.subject = c.subject
        group by 1, 2
        having sum(case when s.exam_date = c.last_date then s.score else 0 end) > sum(case when s.exam_date = c.first_date then s.score else 0 end)


    )
select * 
from cte_2
order by student_id, subject 
