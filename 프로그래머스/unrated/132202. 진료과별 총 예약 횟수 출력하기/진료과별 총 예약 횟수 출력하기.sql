-- 코드를 입력하세요
SELECT mcdp_cd as 진료과코드, count(pt_no) as 5월예약건수
from appointment
where extract(year from apnt_ymd) = 2022 and extract(month from apnt_ymd) = 05
group by mcdp_cd
order by 5월예약건수 asc, 진료과코드 asc