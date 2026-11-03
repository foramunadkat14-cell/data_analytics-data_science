# Assignment Question

import pandas as pd

# Creating Spotify playlist DataFrame
data = {
    "playlist_name": [
        "Chill Hits",
        "Workout Mix",
        "Romantic Songs",
        "Chill Hits",
        "Workout Mix"
    ],
    "creator": [
        "Meetu",
        "Rahul",
        "Amit",
        "Meetu",
        "Rahul"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Removing exact duplicate rows
cleaned_df = df.drop_duplicates()

print("\nCleaned DataFrame:")
print(cleaned_df)

# Output:
# Original DataFrame:
#     playlist_name  creator
# 0      Chill Hits    Meetu
# 1     Workout Mix    Rahul
# 2  Romantic Songs    Amit
# 3      Chill Hits    Meetu
# 4     Workout Mix    Rahul
#
# Cleaned DataFrame:
#     playlist_name  creator
# 0      Chill Hits    Meetu
# 1     Workout Mix    Rahul
# 2  Romantic Songs    Amit