/* Write your T-SQL query statement below */
select W2.id from Weather W1 join Weather W2 on DATEDIFF(day,w1.recordDate, w2.recordDate) = 1 where W2.temperature > W1.temperature