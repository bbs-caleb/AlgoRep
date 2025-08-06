with national_average as (
    select avg(price) as avg from Listings 
)

    , city_averages as (
        select city, avg(price) as avg_city_price
        from Listings
        group by 1
    )

    select city
    from city_averages
    where avg_city_price > (select avg from national_average)
    order by city 
