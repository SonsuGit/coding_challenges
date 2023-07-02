-- 코드를 입력하세요
SELECT book.category, sum(book_sales.sales) as total_sales
from book_sales
join book on book.book_id = book_sales.book_id
where date_format(book_sales.sales_date, '%Y-%m') = '2022-01'
group by category
order by book.category asc