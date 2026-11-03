# Assignment Question

import pandas as pd

# Creating Spotify user DataFrame
df = pd.DataFrame({
    "user": ["A", "B", "C", "D", "E", "F"],
    "is_premium": [True, "False", 1, 0, "yes", "no"]
})

# Converting mixed values into boolean type
df["is_premium"] = df["is_premium"].apply(
    lambda x: str(x).lower() in ["true", "1", "yes"]
)

print("Updated Spotify User Data:")
print(df)

print("\nData Types:")
print(df.dtypes)

# Output:
#   user  is_premium
# 0    A        True
# 1    B       False
# 2    C        True
# 3    D       False
# 4    E        True
# 5    F       False
#
# user          object
# is_premium      bool