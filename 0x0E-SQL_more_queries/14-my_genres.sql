-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name AS name
FROM tv_genres
INNER JOIN tv_show_genres AS tsg ON tv_genres.id = tsg.genre_id
INNER JOIN tv_shows ON tsg.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
