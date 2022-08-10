-- get count grouped by score
SELECT score, count(score) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
