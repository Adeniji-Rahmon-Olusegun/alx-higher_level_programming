--  lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT name
FROM cities
WHERE state_id = (
	SELECT id FROM cities WHERE name = 'California'
);
