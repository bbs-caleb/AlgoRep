select
    b.book_id,
    b.name
from Books b
left join Orders o
    on o.book_id = b.book_id
   and o.dispatch_date >  '2019-06-23'::date - interval '1 year'
   and o.dispatch_date <= '2019-06-23'::date
where b.available_from <= '2019-06-23'::date - interval '1 month'
group by b.book_id, b.name
having coalesce(sum(o.quantity), 0) < 10;
