-- Write your MySQL query statement below
SELECT name 
FROM customer
WHERE id NOT IN ( SELECT id
    FROM customer
    WHERE referee_id = 2);


-- Other Good Answers Found in Solutions
select name from customer
where referee_id != 2 or referee_id is null;

-- here COALESCE is used to replace NULL values with zero before checking whether it is equal to 2 or not.
SELECT name
FROM Customer
WHERE COALESCE(referee_id,0) != 2;