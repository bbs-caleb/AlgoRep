select s1.sub_id as post_id, coalesce(count(distinct s2.sub_id), 0) as number_of_comments
from Submissions s1
left join Submissions s2 
    on s1.sub_id = s2.parent_id
where s1.parent_id is null 
group by 1 
order by post_id  