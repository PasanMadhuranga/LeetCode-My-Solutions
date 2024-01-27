-- Write your MySQL query statement below
SELECT ROUND((COUNT(IF(d.order_date = d.customer_pref_delivery_date, 1, NULL))/COUNT(d.customer_id)) * 100, 2) AS immediate_percentage 
FROM (SELECT customer_id , MIN(order_date) min_date
    FROM Delivery
    GROUP BY customer_id) fo
JOIN Delivery d ON d.customer_id = fo.customer_id AND d.order_date = fo.min_date 

-- Another Solution found in the discussion section
Select 
    round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
  Select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);
-- Expression: round(avg(order_date = customer_pref_delivery_date)*100, 2)
-- order_date = customer_pref_delivery_date: This condition checks whether 
-- the order_date is equal to customer_pref_delivery_date for each row. 
-- In MySQL, a boolean expression like this returns 1 if true, and 0 if false.