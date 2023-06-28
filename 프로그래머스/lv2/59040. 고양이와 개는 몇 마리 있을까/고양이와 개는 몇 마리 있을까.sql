-- 코드를 입력하세요
SELECT animal_type, count(ANIMAL_id)
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE