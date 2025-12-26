with failed as (
    select  fail_date, lag(fail_date) over (order by fail_date) as prev_date
    from Failed
    where fail_date >= '2019-01-01' and fail_date < '2020-01-01'
)

, failed_flags as (
    select fail_date, prev_date, 
            case when prev_date is null or fail_date - prev_date = 1 
                        then 0 else 1 
            end as is_continious
    from failed
)

, failed_grp as (
    select fail_date, prev_date, sum(is_continious) over (order by fail_date) as grp 
    from failed_flags
)


, success as (
    select  success_date, lag(success_date) over (order by success_date) as prev_date
    from Succeeded
    where success_date >= '2019-01-01' and success_date < '2020-01-01'
)

, sucess_flags as (
    select success_date, 
            case when prev_date is null or success_date - prev_date = 1 
                        then 0 else 1 
            end as is_continious
    from success
)

, success_grp as (
    select success_date, sum(is_continious) over (order by success_date) as grp 
    from sucess_flags
)

select 'failed' as period_state, min(fail_date) as start_date, max(fail_date) as end_date
from failed_grp 
group by grp 

union all 

select 'succeeded' as period_state, min(success_date) as start_date, max(success_date) as end_date
from success_grp 
group by grp 
order by start_date 