with cte as (
    select t.task_id, gs.count_
    from Tasks t 
    cross join lateral generate_series(1, t.subtasks_count) gs(count_)
    where not exists (select 1 from Executed e where e.task_id = t.task_id and e.subtask_id = gs.count_)
)
select task_id, count_ as subtask_id 
from cte 
order by task_id, subtask_id