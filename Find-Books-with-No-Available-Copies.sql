1select  
2        lb.book_id,
3        lb.title,
4        lb.author,
5        lb.genre,
6        lb.publication_year,
7        lb.total_copies as current_borrowers
8from library_books lb 
9inner join borrowing_records b 
10    on lb.book_id = b.book_id
11group by 1, 2, 3, 4, 5, 6
12having lb.total_copies = sum(case when return_date is null then 1 else 0 end)
13order by current_borrowers desc, lb.title;
14