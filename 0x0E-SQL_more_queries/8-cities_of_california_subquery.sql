-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
select 'id', 'name' FROM cities
	WHERE state_id = (
		select id FROM states
		WHERE 'name' = 'Carlifornia')
	ORDER BY id ASC;
