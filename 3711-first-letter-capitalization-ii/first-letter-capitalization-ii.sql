with counters as (
    select  
            content_id,
            content_text,
            gs.i as ind,
            substring(u.content_text from gs.i for 1) as char_
    from user_content u 
    cross join generate_series(1, length(u.content_text)) as gs(i))

    , cte as (
        select 
                content_id, 
                content_text, 
                ind,
                char_,
                lag(char_) over (partition by content_id
                            order by ind) as prev_char
        from counters
    )
    , cte2 as (
        select 
                content_id,
                content_text,
                case
                    when prev_char is null or prev_char = ' ' 
                        then upper(char_) 
                    when prev_char = '-'
                        then upper(char_)
                    else lower(char_)
                end as char
        from cte
    )

    select  
            content_id,
            content_text as original_text,
            string_agg(char, '') as converted_text
    from cte2
    group by 1, 2
