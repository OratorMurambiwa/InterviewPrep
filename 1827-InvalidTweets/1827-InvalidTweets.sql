-- Last updated: 31/12/2025, 18:43:36
# Write your MySQL query statement below
Select tweet_id
from Tweets
where length(content) > 15;