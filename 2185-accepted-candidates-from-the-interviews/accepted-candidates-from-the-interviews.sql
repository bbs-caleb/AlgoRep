
    select c.candidate_id
    from Candidates c 
    inner join Rounds r 
        on c.years_of_exp >= 2 and c.interview_id = r.interview_id
    group by c.candidate_id
    having sum(r.score) > 15

