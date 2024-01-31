-- Write your MySQL query statement below
SELECT ROUND((COUNT(second_date) / COUNT(DISTINCT(a.player_id))), 2) AS fraction 
FROM Activity a
LEFT JOIN (
    SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY) AS second_date 
    FROM Activity
    GROUP BY player_id 
) s ON a.player_id = s.player_id AND a.event_date = s.second_date


-- Another solution found in the discussion section
SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN (
    SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id)