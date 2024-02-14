-- List all record of second table 
--where the name is not NULL ordered by the score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
