-- create a table where id column is not null
CREATE TABLE IF NOT EXISTS unique_id(
id INT UNIQUE DEFAULT (1), 
name VARCHAR(256));
