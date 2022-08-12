-- lists all the cities of California that can be found in the database
SELECT id, name
FROM `hbtn_0d_usa`.`cities`
WHERE state_id = (SELECT id
		WHERE name = "California"
);
