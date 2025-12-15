1with avg_by_type as (
2    select
3        event_type,
4        avg(occurrences::numeric) as avg_occ
5    from events
6    group by event_type
7)
8    , above_avg as (
9            select
10                e.business_id,
11                e.event_type
12            from events e
13            join avg_by_type a
14            on a.event_type = e.event_type
15            where e.occurrences::numeric > a.avg_occ
16)
17select
18    business_id
19from above_avg
20group by business_id
21having count(distinct event_type) > 1