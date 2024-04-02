/* Write your T-SQL query statement below */

select P.product_id, 
isnull(round(cast(sum(units*price) as float)/ cast(sum(units) as float), 2), 0) as average_price 
from Prices P left join UnitsSold US on P.product_id = US.product_id
and US.purchase_date between P.start_date and P.end_date
group by P.product_id
