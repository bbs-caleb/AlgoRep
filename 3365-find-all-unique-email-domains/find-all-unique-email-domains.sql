select 
    split_part(email, '@', -1) as email_domain,
    count(*) as count
from Emails 
where split_part(email, '.', -1) = 'com'
group by 1
order by email_domain;