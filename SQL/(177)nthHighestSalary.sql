CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select max(Salary)
      from Employee e1
      where (select count(distinct Salary) from Employee e2 where e2.Salary>e1.Salary) = N-1
  );
END

