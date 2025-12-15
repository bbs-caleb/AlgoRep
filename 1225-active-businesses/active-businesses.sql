with avg_by_type as (
    select
        event_type,
        avg(occurrences::numeric) as avg_occ
    from events
    group by event_type
)
    , above_avg as (
            select
                e.business_id,
                e.event_type
            from events e
            join avg_by_type a
            on a.event_type = e.event_type
            where e.occurrences::numeric > a.avg_occ
)
select
    business_id
from above_avg
group by business_id
having count(distinct event_type) > 1