-- Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary NOT IN (
    SELECT MAX(salary)
    FROM Employee)


-- Another solution found in the discussion section
WITH CTE AS
			(SELECT Salary, RANK () OVER (ORDER BY Salary desc) AS RANK_desc
			   FROM Employee)
SELECT MAX(salary) AS SecondHighestSalary
  FROM CTE
 WHERE RANK_desc = 2