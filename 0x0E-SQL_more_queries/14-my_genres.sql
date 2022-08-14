-- lists all shows contained in hbtn_0d_tvshows
SELECT name
FROM tv_genres
WHERE id IN
	(SELECT tv_show_genres.genre_id
	FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = "Dexter")
ORDER BY name ASC;
