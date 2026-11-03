# Assignment Question

import pandas as pd

# Loading trending songs data from JSON file
df = pd.read_json("trending_songs.json")

# Displaying column names
print("Column Names:")
print(df.columns)

# Displaying data types
print("\nData Types:")
print(df.info())

# Output:
# Column Names:
# Displays all column names from the JSON dataset.
#
# Data Types:
# Displays column names, non-null values and data types.