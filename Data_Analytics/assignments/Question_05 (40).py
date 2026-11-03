# Assignment Question

import pandas as pd

# Creating order DataFrame
df = pd.DataFrame({
    "order_date": [
        "2024-06-01",
        "2024-06-03",
        "2024-06-08",
        "2024-06-10",
        "2024-06-15"
    ]
})

# Converting order_date into datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Creating weekend feature
df["is_weekend"] = df["order_date"].dt.dayofweek >= 5

print("Updated Order DataFrame:")
print(df)

# Output:
#   order_date  is_weekend
# 0 2024-06-01       True
# 1 2024-06-03       False
# 2 2024-06-08       True
# 3 2024-06-10       False
# 4 2024-06-15       True