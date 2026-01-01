-- Last updated: 31/12/2025, 18:43:37
# Write your MySQL query statement below
SELECT customer_id, Count(*) as count_no_trans
FROM Visits as v
LEFT JOIN Transactions as t
ON v.visit_id = t.visit_id
where transaction_id IS NULL
GROUP BY customer_id;