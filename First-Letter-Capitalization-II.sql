1with counters as (
2    select  
3            content_id,
4            content_text,
5            gs.i as ind,
6            substring(u.content_text from gs.i for 1) as char_
7    from user_content u 
8    cross join generate_series(1, length(u.content_text)) as gs(i))
9
10    , cte as (
11        select 
12                content_id, 
13                content_text, 
14                ind,
15                char_,
16                lag(char_) over (partition by content_id
17                            order by ind) as prev_char
18        from counters
19    )
20    , cte2 as (
21        select 
22                content_id,
23                content_text,
24                case
25                    when prev_char is null or prev_char = ' ' 
26                        then upper(char_) 
27                    when prev_char = '-'
28                        then upper(char_)
29                    else lower(char_)
30                end as char
31        from cte
32    )
33
34    select  
35            content_id,
36            content_text as original_text,
37            string_agg(char, '') as converted_text
38    from cte2
39    group by 1, 2
40