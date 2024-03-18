-- Write your MySQL query statement below
SELECT person_name
FROM Queue
WHERE turn IN (
    SELECT IFNULL((SELECT MIN(turn) - 1
    FROM (
        SELECT *, (
        SELECT SUM(weight)
        FROM Queue q2
        WHERE q2.turn <= q1.turn) tot_weight
        FROM Queue q1
    ) ws
    WHERE tot_weight > 1000), MAX(turn))
    FROM Queue
)


-- Other solutions found in the discussion section
SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1

-- ------------------------------------------------
SELECT a.person_name
FROM
(
    SELECT person_name,
    sum(weight) OVER (ORDER BY turn ROWS unbounded preceding) AS running_sum
    FROM Queue
) a
WHERE a.running_sum <= 1000
ORDER BY a.running_sum DESC
LIMIT 1


