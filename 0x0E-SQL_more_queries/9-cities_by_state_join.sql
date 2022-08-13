-- lists all cities contained in the database hbtn_0d_usa.
SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN state as s
ON c.state_id = s.id;
