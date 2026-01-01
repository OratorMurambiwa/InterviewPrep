-- Last updated: 31/12/2025, 18:43:40
# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales as s
LEFT JOIN Product as p
ON s.product_id = p.product_id;