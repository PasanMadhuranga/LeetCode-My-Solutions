-- Write your MySQL query statement below
SELECT s.user_id, ROUND(COALESCE(confirmed / total, 0),2) confirmation_rate
FROM Signups s
LEFT JOIN (SELECT user_id, COUNT(time_stamp) total
    FROM Confirmations 
    GROUP BY user_id) ct USING(user_id)
LEFT JOIN (
    SELECT user_id, COUNT(time_stamp) confirmed
    FROM Confirmations 
    WHERE action = "confirmed"
    GROUP BY user_id) cc USING(user_id)


-- Another solution found in the discussion section
SELECT s.user_id, ROUND(AVG(IF(c.action="confirmed",1,0)),2) as confirmation_rate
FROM Signups s 
LEFT JOIN Confirmations c USING(user_id)
GROUP BY user_id;

