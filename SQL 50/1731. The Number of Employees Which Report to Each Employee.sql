-- Write your MySQL query statement below
SELECT reports_to employee_id, 
    (SELECT name FROM Employees e2 WHERE e2.employee_id = e1.reports_to) name
    ,COUNT(reports_to) reports_count, ROUND(AVG(age)) average_age
FROM Employees e1
WHERE reports_to IS NOT NULL
GROUP BY reports_to
ORDER BY e1.reports_to


-- Another faster solution found in the discussion section
SELECT E1.employee_id, E1.name, COUNT(E2.employee_id) reports_count,
    ROUND(AVG(E2.age)) average_age 
FROM Employees E1 
INNER JOIN Employees E2 ON E1.employee_id = E2.reports_to 
GROUP BY E1.employee_id
ORDER BY employee_id