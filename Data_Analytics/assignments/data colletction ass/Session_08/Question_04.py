# Assignment Question

import pandas as pd

# Creating Instagram usernames DataFrame
df = pd.DataFrame({
    "username": [
        "insta_queen",
        "insta-queen",
        "instaqueen",
        "insta_king",
        "insta-king"
    ]
})

# Standardizing username formats
df["username"] = df["username"].replace({
    "insta_queen": "instaqueen",
    "insta-queen": "instaqueen",
    "insta_king": "instaking",
    "insta-king": "instaking"
})

print("Standardized Usernames:")
print(df)

# Output:
#      username
# 0   instaqueen
# 1   instaqueen
# 2   instaqueen
# 3     instaking
# 4     instaking