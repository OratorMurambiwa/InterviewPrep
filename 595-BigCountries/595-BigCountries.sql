-- Last updated: 29/12/2025, 03:02:55
# Write your MySQL query statement below
select name, population, area
from World
where area >= 3000000
    OR population >= 25000000;
