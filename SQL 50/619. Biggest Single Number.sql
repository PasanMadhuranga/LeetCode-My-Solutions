-- Write your MySQL query statement below
SELECT MAX(mn.num) num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1) mn