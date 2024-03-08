-- Write your MySQL query statement below
SELECT activity_date day, COUNT(DISTINCT(user_id)) active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) AND "2019-07-27"
GROUP BY activity_date


-- Another solution found in the discussion section
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY activity_date
HAVING activity_date <= '2019-07-27' AND activity_date > '2019-06-27'