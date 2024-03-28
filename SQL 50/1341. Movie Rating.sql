-- Write your MySQL query statement below
(SELECT u.name AS results
FROM MovieRating mr
JOIN Users u USING (user_id)
GROUP BY mr.user_id
ORDER BY COUNT(mr.movie_id) DESC, u.name ASC
LIMIT 1)

UNION ALL

(SELECT m.title AS results
FROM MovieRating mr
JOIN Movies m USING (movie_id)
WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY mr.movie_id
ORDER BY AVG(mr.rating) DESC, m.title ASC
LIMIT 1)