-- Write your MySQL query statement below
SELECT DISTINCT(L1.num) ConsecutiveNums
FROM Logs L1
JOIN Logs L2 ON L1.id + 1 = L2.id AND L1.num = L2.num
JOIN Logs L3 ON L1.id + 2 = L3.id AND L1.num = L3.num


-- Other solutions found in the discussion section
SELECT DISTINCT num AS ConsecutiveNums
FROM Logs
WHERE (Id + 1, num) IN (SELECT * FROM Logs) AND (Id + 2, num) IN (SELECT * FROM Logs)

-- with cte as (...) - This is the CTE definition that creates a temporary result set named cte.
-- Inside the CTE:
-- select num - This selects the num column from the Logs table.
-- lead(num,1) over() as num1 - The LEAD() function is a window function 
-- that returns the value of num from the row that is a specified number of rows ahead. 
-- In this case, lead(num,1) gets the value of num from the next row.
-- lead(num,2) over() as num2 - Similarly, this gets the value of num from two rows ahead.

WITH cte AS (
    SELECT num,
    lead(num,1) OVER() num1,
    lead(num,2) OVER() num2
    FROM logs

)

SELECT DISTINCT num ConsecutiveNums FROM cte WHERE (num=num1) AND (num=num2)

