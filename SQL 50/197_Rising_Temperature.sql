-- Write your MySQL query statement below
SELECT b.id
FROM Weather a
INNER JOIN Weather b ON DATE_ADD(a.recordDate, INTERVAL 1 DAY) = b.recordDate
WHERE b.temperature > a.temperature


-- Another solution found in the discussion section
SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;