-- list score and name in a table where name is not Null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
