import sqlite3

# movies.db is now located in the ai directory
con = sqlite3.connect("movies.db")
cur = con.cursor()

# this is a tuple, while (2008) is an int
year = (2008,)
res = cur.execute("SELECT title FROM movies WHERE year = ? LIMIT 10;", year)
for row in res:
    print(row)