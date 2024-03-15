-- script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres tsg
	LEFT JOIN tv_shows ts ON tsg.show_id = ts.id
       ORDER BY ts.title ASC, tsg.genre_id ASC;	
