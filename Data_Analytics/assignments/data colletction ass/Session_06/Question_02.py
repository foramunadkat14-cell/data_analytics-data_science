# Assignment Question

import pandas as pd
import numpy as np

# Creating IPL player statistics dataset
data = {
    "player_name": ["Virat", "Rohit", "Dhoni", "Hardik", "Gill"],
    "runs": [850, np.nan, 650, 450, np.nan],
    "matches": [14, 12, np.nan, 10, 13],
    "wickets": [0, 2, 1, np.nan, 0]
}

df = pd.DataFrame(data)

# Displaying shape before dropping missing values
print("Shape Before Dropping:", df.shape)

# Removing rows with any missing values
df = df.dropna(axis=0, how="any")

# Displaying shape after dropping missing values
print("Shape After Dropping:", df.shape)

print("\nUpdated DataFrame:")
print(df)

# Output:
# Shape Before Dropping: (5, 4)
# Shape After Dropping: (1, 4)
#
# Updated DataFrame:
#   player_name   runs   matches   wickets
# 0 Virat         850.0  14.0      0.0