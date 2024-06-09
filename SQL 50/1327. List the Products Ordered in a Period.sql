SELECT p.product_name, o.unit
FROM (SELECT product_id, SUM(unit) unit
FROM Orders
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29' 
GROUP BY product_id
HAVING unit >= 100) o
JOIN Products p USING(product_id)


-- Another Solution found in the discussion section
SELECT p.product_name, o.unit
FROM (SELECT product_id, SUM(unit) unit
FROM Orders
WHERE LEFT(order_date, 7) = '2020-02' 
GROUP BY product_id
HAVING unit >= 100) o
JOIN Products p USING(product_id)

