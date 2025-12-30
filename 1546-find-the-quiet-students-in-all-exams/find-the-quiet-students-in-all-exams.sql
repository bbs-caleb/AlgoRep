with min_max as (
    select exam_id, min(score) min_, max(score) max_
    from Exam
    group by exam_id
)
select s.student_id, s.student_name
from Student s
where exists (
    select 1
    from Exam e
    where e.student_id = s.student_id
)
and not exists (
    select 1
    from Exam e
    join min_max m on e.exam_id = m.exam_id
    where e.student_id = s.student_id
      and (e.score = m.min_ or e.score = m.max_)
)
order by s.student_id;
