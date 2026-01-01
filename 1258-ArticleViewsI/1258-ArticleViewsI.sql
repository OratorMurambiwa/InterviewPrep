-- Last updated: 31/12/2025, 18:43:39
# Write your MySQL query statement below
SELECT distinct author_id as id
from Views
Where Views.author_id = Views.viewer_id
ORDER BY id;