-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN,'N') as FREEZER_YN
from FOOD_WAREHOUSE
where left(address, 3) = '경기도'
order by warehouse_id asc