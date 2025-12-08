select  
        lb.book_id,
        lb.title,
        lb.author,
        lb.genre,
        lb.publication_year,
        lb.total_copies as current_borrowers
from library_books lb 
inner join borrowing_records b 
    on lb.book_id = b.book_id
group by 1, 2, 3, 4, 5, 6
having lb.total_copies = sum(case when return_date is null then 1 else 0 end)
order by current_borrowers desc, lb.title;
