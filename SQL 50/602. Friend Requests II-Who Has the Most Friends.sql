-- The main difference between UNION and UNION ALL is that 
-- UNION has the ability to remove duplicate rows from the table 
-- while UNION ALL cannot. 

SELECT id, SUM(friends) num
FROM (SELECT requester_id id, COUNT(accepter_id) friends
    FROM RequestAccepted
    GROUP BY (requester_id)
    UNION ALL
    SELECT accepter_id id, COUNT(requester_id) friends
    FROM RequestAccepted
    GROUP BY (accepter_id)) f
GROUP BY id
ORDER BY num DESC
LIMIT 1


-- Another Solution found in the discussion section
-- The WITH clause is used to create a CTE (Common Table Expression) named base. 
-- This CTE is a temporary result set that we can refer to within the rest of the query.
WITH base AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)

SELECT id, COUNT(id) num
FROM base
GROUP BY id
ORDER BY num DESC
LIMIT 1