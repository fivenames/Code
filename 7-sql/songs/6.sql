--query that lists the names of songs that are by Post Malone.

SELECT name FROM songs WHERE id = (SELECT id FROM artists WHERE name = 'Post Malone');