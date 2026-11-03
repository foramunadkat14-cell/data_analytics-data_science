# Assignment Question

import pandas as pd

# Loading Zomato restaurant ratings dataset
df = pd.read_csv("zomato_ratings.csv")

# Calculating Q1 and Q3
Q1 = df["user_rating"].quantile(0.25)
Q3 = df["user_rating"].quantile(0.75)

# Calculating IQR
IQR = Q3 - Q1

# Calculating lower and upper limits
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Detecting outliers
outliers = df[(df["user_rating"] < lower) |
              (df["user_rating"] > upper)]

# Printing outlier indices
print("Outlier Indices:")
print(outliers.index.tolist())

# Output:
# Outlier Indices:
# Displays the indices of detected outliers.