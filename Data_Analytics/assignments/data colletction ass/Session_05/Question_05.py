# Assignment Question

import pandas as pd

# Creating today's orders DataFrame
today_orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "item": ["Pizza", "Burger", "Sandwich"],
    "price": [250, 150, 100]
})

# Creating yesterday's orders DataFrame
yesterday_orders = pd.DataFrame({
    "order_id": [104, 105, 106],
    "item": ["Pasta", "Fries", "Dosa"],
    "price": [200, 80, 120]
})

# Concatenating both DataFrames
combined_orders = pd.concat(
    [today_orders, yesterday_orders],
    ignore_index=True
)

print("Combined Orders:")
print(combined_orders)

# Output:
#    order_id      item  price
# 0       101     Pizza    250
# 1       102    Burger    150
# 2       103  Sandwich    100
# 3       104     Pasta    200
# 4       105     Fries     80
# 5       106      Dosa    120