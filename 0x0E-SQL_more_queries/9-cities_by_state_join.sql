-- lists all cities contained in the database hbtn_0d_usa.
SELECT c.id, c.name, s.name
FROM cities AS c
FULL JOIN states as s
ON c.state_id = s.id
ORDER BY c.id;
