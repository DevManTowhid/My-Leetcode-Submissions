# Write your MySQL query statement below
select 
DATE_FORMAT(trans_date , '%Y-%m') AS month,
country,
count(*) as trans_count,
count(CASE WHEN state = 'approved' THEN 1 END) as approved_count,

sum(amount) as trans_total_amount,
sum(CASE WHEN state = 'approved' THEN amount else 0 END) as approved_total_amount

from Transactions


group by month, country