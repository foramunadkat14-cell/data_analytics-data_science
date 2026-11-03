# Assignment Question

import pandas as pd

# Creating order DataFrame
df = pd.DataFrame({
    "order_date": [
        "2024-06-01",
        "2024-06-02",
        "2024-06-03",
        "2024-06-08",
        "2024-06-10",
        "2024-06-15"
    ],
    "order_id": [101, 102, 103, 104, 105, 106]
})

# Converting order_date into datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Setting order_date as index
df.set_index("order_date", inplace=True)

# Calculating weekly number of orders
weekly_orders = df.resample("W").size()

print("Weekly Orders:")
print(weekly_orders)

# Output:
# 2024-06-02    2
# 2024-06-09    2
# 2024-06-16    2