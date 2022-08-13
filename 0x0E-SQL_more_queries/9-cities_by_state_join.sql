-- lists all cities contained in the database hbtn_0d_usa.
SELECT c.id, c.name, s.name
FROM cities AS c
FULL OUTER JOIN states as s
ON c.id = s.id
ORDER BY c.id;
