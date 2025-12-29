-- Last updated: 29/12/2025, 03:02:46
# Write your MySQL query statement below
select product_id
from Products
where low_fats = 'Y' 
    AND recyclable = 'Y';