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

# Checking missing values using isnull()
print("Missing Values:")
print(df.isnull().sum())

# Checking non-missing values using notnull()
print("\nNon-Missing Values:")
print(df.notnull().sum())

# Output:
# Missing Values:
# player_name    0
# runs           2
# matches        1
# wickets        1
#
# Non-Missing Values:
# player_name    5
# runs           3
# matches        4
# wickets        4