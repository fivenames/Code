--query to list the names of all songs in the database.

--sqlite3 songs.db
--.schema {
--    CREATE TABLE songs (
--    id INTEGER,
--    name TEXT,
--    artist_id INTEGER,
--    danceability REAL,
--    energy REAL,
--    key INTEGER,
--    loudness REAL,
--    speechiness REAL,
--    valence REAL,
--    tempo REAL,
--    duration_ms INTEGER
-- );
--CREATE TABLE artists (
--    id INTEGER,
--    name TEXT
--);}

SELECT name FROM songs;