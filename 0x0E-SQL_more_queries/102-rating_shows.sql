-- A script that lists all shows from hbtn_0d_tvshows_rate  and displays the
--  total ratings linked to each
SELECT `tv_shows`.`title`, SUM(`tv_show_ratings`.`rate`) AS `rating`
    FROM tv_show_ratings
    RIGHT JOIN tv_shows ON `tv_show_ratings`.`show_id` = `tv_shows`.`id`
    GROUP BY `tv_shows`.`title`
    ORDER BY `rating` DESC;
