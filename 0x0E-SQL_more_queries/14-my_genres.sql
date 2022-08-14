-- lists all shows contained in hbtn_0d_tvshows
SELECT name
FROM tv_genres
INNER JOIN
	(tv_shows
	INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id)
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = "Dexter"
ORDER BY name ASC;
