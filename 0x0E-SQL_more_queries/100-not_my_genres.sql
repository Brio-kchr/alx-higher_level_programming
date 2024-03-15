-- A script that lists all genres not of the show Dexter from hbtn_0d_tvshows
SELECT `tv_genres`.`name` AS `name` FROM tv_genres
    WHERE `name` NOT IN (
        SELECT `tv_genres`.`name` AS `name`
            FROM tv_show_genres
            INNER JOIN tv_genres
                ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
            INNER JOIN tv_shows
                ON `tv_show_genres`.`show_id` = `tv_shows`.`id`
            WHERE `tv_shows`.`title` = 'Dexter'
    )
    ORDER BY `name` ASC;
