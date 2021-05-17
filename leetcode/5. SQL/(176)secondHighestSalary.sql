-- # Simple solution 
select max(Salary) as SecondHighestSalary
from Employee where Salary not in (select max(salary) from Employee)

-- # Better solution if trying to find Nth highest, just change the 1 to whatever N-1 you are looking for 
SELECT MAX(Salary) SecondHighestSalary
FROM Employee e1
WHERE (SELECT COUNT(DISTINCT Salary) FROM Employee e2 WHERE e2.Salary > e1.Salary) = 1;