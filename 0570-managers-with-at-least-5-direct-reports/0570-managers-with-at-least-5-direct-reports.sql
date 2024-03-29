/* Write your T-SQL query statement below */
select E2.name from Employee E1 inner join Employee E2 on E2.id = E1.managerId
group by E2.name, E2.id
having count(E1.id) >= 5