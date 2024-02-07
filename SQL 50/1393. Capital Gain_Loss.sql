-- Write your MySQL query statement below
SELECT s.stock_name, ((
    SELECT SUM(sn.price)
    FROM Stocks sn
    WHERE sn.stock_name = s.stock_name AND sn.operation = "Sell") - SUM(s.price)) AS capital_gain_loss 
FROM Stocks s
WHERE s.operation = "Buy"
GROUP BY s.stock_name


-- Another solution found in the discussion section
SELECT stock_name, SUM(
    CASE
        WHEN operation = 'Buy' THEN -price
        ELSE price
    END
) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name


SELECT stock_name
, sum(if(operation = 'Buy', -1, 1) * price) AS capital_gain_loss
FROM stocks
GROUP BY stock_name