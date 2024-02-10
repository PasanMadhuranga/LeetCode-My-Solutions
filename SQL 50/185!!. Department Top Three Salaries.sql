-- Write your MySQL query statement below
SELECT d.name Department, e1.name Employee, e1.Salary
FROM Employee e1
JOIN Department d ON e1.departmentId = d.id
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.Salary) 
    FROM Employee e2 
    WHERE e2.departmentId = e1.departmentId AND e1.Salary < e2.Salary)


-- Another solution found in the discussion section
-- The DENSE_RANK() function is applied to the rows of each partition defined by the PARTITION BY clause, 
-- in a specified order, defined by ORDER BY clause. It resets the rank when the partition boundary is crossed.
SELECT d.name AS Department, e.name AS Employee, e.Salary
FROM Department d
JOIN (
    SELECT *,
           DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY Salary DESC) AS dr
    FROM Employee
) e ON d.id = e.departmentId
WHERE e.dr <= 3
