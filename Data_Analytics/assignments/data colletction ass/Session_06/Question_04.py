# Assignment Question

import pandas as pd
import numpy as np

# Creating Zomato restaurant ratings dataset
data = {
    "restaurant": ["A", "B", "C", "D", "E", "F"],
    "ratings": [4.5, np.nan, 3.8, np.nan, np.nan, 4.2]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Applying forward fill
df["ratings"] = df["ratings"].ffill()

# Applying backward fill for remaining missing values
df["ratings"] = df["ratings"].bfill()

print("\nUpdated Dataset:")
print(df)

# Output:
# Original Dataset:
#   restaurant  ratings
# 0     A        4.5
# 1     B        NaN
# 2     C        3.8
# 3     D        NaN
# 4     E        NaN
# 5     F        4.2
#
# Updated Dataset:
#   restaurant  ratings
# 0     A        4.5
# 1     B        4.5
# 2     C        3.8
# 3     D        3.8
# 4     E        3.8
# 5     F        4.2