
        select title as results 
        from (
            select  
                    Movies.movie_id,
                    Movies.title,
                    avg(rating) as avg_rating, 
                    row_number() over (order by avg(rating) DESC, title) as rk 
            from MovieRating 
            join Movies on Movies.movie_id = MovieRating.movie_id 
            where to_char(created_at, 'YYYY-MM') = '2020-02'
            group by 1, 2) 
        where rk = 1 

        union all 

        select name as results 
        from (
            select 
                    u.user_id,
                    u.name,
                    count(distinct movie_id) as total,
                    row_number() over (order by count(distinct movie_id) DESC, u.name ) rl

            from MovieRating m
            join Users u on u.user_id = m.user_id 
            group by 1, 2)
        where rl = 1 