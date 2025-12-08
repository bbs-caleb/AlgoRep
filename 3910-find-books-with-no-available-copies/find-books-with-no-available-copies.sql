with borrowed as (
    select  book_id,
            count(*) as total 
    from borrowing_records 
    where return_date is null
    group by 1 
)
select  
        lb.book_id,
        lb.title,
        lb.author,
        lb.genre, 
        lb.publication_year,
        b.total as current_borrowers
from library_books lb 
inner join borrowed b 
        on lb.book_id = b.book_id
                and lb.total_copies = b.total
order by current_borrowers desc, lb.title;
