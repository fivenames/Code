-- query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.

-- Order by foreign values.
SELECT title FROM movies, ratings WHERE movies.id IN (SELECT movie_id FROM stars
WHERE person_id = (SELECT id FROM people WHERE name = 'Chadwick Boseman'))
AND movies.id = ratings.movie_id ORDER BY rating DESC LIMIT 5;