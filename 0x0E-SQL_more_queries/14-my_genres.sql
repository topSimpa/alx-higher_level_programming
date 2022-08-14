-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_show_genres.name
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.name == "Dexter"
ORDER BY tv_show_genres.name ASC;
