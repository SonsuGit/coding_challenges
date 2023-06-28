-- 코드를 입력하세요
SELECT user_id, product_id
from ONLINE_SALE

group by user_id, product_id
having count(sales_amount)>=2
ORDER BY USER_ID ASC, PRODUCT_ID DESC