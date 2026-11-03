# Assignment Question

import pandas as pd
import numpy as np

# Creating IPL player statistics dataset
data = {
    "player_name": ["Virat", "Rohit", "Dhoni", "Hardik", "Gill"],
    "runs": [850, np.nan, 650, 450, np.nan]
}

df = pd.DataFrame(data)

# Calculating mean of runs column
mean_value = df["runs"].mean()

# Replacing missing values with mean
df["runs"] = df["runs"].fillna(mean_value)

print("Updated Runs Column:")
print(df["runs"])

# Output:
# Updated Runs Column:
# 0    850.000000
# 1    650.000000
# 2    650.000000
# 3    450.000000
# 4    650.000000