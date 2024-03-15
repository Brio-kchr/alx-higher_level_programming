-- script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities C
	LEFT OUTER JOIN states S
	ON C.state_id = S.id
	ORDER BY C.id ASC;
