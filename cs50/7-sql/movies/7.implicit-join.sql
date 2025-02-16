-- query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title.

SELECT title, rating FROM movies, ratings WHERE year = 2010 AND movies.id = ratings.movie_id ORDER BY rating DESC, title ASC;