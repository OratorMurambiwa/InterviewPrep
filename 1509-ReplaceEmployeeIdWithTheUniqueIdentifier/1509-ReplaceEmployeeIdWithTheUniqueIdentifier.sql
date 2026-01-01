-- Last updated: 31/12/2025, 18:43:38
# Write your MySQL query statement below
SELECT e2.unique_id, e1.name
from Employees as e1
LEFT JOIN EmployeeUNI as e2
ON e1.id = e2.id;