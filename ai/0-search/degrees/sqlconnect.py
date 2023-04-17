import sqlite3

def connect_to_db(directory, data):
    # Connect to the database
    con = sqlite3.connect(directory)

    # Create a cursor and execute the query
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {data};")

    # Get the names of the columns from the cursor description,
    column_names = [desc[0] for desc in cur.description]

    # Yield rows as dictionaries
    for row in cur.fetchall():
        yield dict(zip(column_names, row))

    # Close the cursor and connection
    cur.close()
    con.close()