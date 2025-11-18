select abs(max(case when department = 'Marketing' then salary else -1 end) - max(case when department = 'Engineering' then salary else -1 end)) as salary_difference
from Salaries