# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;


-- another solution I found in solutions
select area,population,name
from world
where area>=3000000
union
select area,population,name
from world
where population>=25000000