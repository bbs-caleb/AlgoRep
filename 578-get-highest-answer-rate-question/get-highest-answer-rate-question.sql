select 
    question_id as survey_log
from SurveyLog
group by question_id
order by coalesce(sum(case when action = 'answer' then 1 end)::numeric / nullif(sum(case when action = 'show' then 1 end), 0), 0) desc, 
            question_id
limit 1