select 
    user_id
from Loans
group by user_id 
having sum(case when loan_type = 'Mortgage' then 1 else 0 end) > 0
        and sum(case when loan_type = 'Refinance' then 1 else 0 end) > 0
order by user_id