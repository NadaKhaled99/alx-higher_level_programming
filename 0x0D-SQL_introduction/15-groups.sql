-- Count the number of occurences of a particular score 
--grouped by score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
