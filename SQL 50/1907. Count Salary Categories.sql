-- Write your MySQL query statement below
SELECT "Low Salary" AS category, COUNT(account_id) accounts_count
FROM Accounts
WHERE income < 20000

UNION 

SELECT "Average Salary" AS category, COUNT(account_id) accounts_count
FROM Accounts
WHERE 20000 <= income AND income <= 50000

UNION

SELECT "High Salary" AS category, COUNT(account_id) accounts_count
FROM Accounts
WHERE income > 50000