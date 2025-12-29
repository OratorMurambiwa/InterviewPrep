-- Last updated: 29/12/2025, 03:02:57
# Write your MySQL query statement below
select name
from Customer
where referee_id IS Null
    OR referee_id != 2;