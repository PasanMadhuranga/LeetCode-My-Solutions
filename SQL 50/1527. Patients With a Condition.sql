-- Write your MySQL query statement below
SELECT *
FROM Patients
WHERE conditions REGEXP ' DIAB1|^DIAB1'


-- Another solution found in the discussion section
SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1'
-- The expression conditions REGEXP '\\bDIAB1' is actually the same as 
-- conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%';, 
