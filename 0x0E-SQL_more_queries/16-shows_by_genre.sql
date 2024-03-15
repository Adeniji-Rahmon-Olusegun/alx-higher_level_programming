--  lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows
LEFT JOIN tv_show_genres AS tsg ON tv_shows.id = tsg.show_id
LEFT JOIN tv_genres ON tv_genres.id = tsg.genre_id
ORDER BY title ASC, name ASC;
