-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title As title
FROM tv_shows
INNER JOIN tv_show_genres AS tsg ON tv_shows.id = tsg.show_id
INNER JOIN tv_genres ON tsg.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
