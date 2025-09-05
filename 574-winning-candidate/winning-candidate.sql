-- Write your PostgreSQL query statement below
select name
from (
  select c.name,
         count(*) as votes,
         rank() over (order by count(*) desc) as rnk
  from candidate c
  join vote v on v.candidateid = c.id
  group by c.id, c.name
) t
where rnk = 1