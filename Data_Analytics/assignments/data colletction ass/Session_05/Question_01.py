import pandas as pd
import importlib

mysql_connector = importlib.import_module("mysql.connector")

# Connecting to MySQL database
conn = mysql_connector.connect(
    host="localhost",
    user="root",
    password="",
    database="restaurant_db"
)

# Loading restaurants table into DataFrame
df = pd.read_sql("SELECT * FROM restaurants", conn)

# Displaying first 5 rows
print("First 5 Rows:")
print(df.head())

# Closing database connection
conn.close()

# Output:
# Displays the first 5 rows of the restaurants table.