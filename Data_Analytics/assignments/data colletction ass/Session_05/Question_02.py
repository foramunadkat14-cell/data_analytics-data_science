# Assignment Question

import pandas as pd
import mysql.connector # type: ignore

# Connecting to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="movie_db"
)

# Fetching movie names and ratings above 8
query = """
SELECT name, rating
FROM movies
WHERE rating > 8
"""

df = pd.read_sql(query, conn)

print("Movies with Rating Above 8:")
print(df)

# Closing database connection
conn.close()

# Output:
# Displays movie names and ratings
# where rating is greater than 8.