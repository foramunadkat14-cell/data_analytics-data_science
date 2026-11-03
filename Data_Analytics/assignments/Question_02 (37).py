# Assignment Question

import pandas as pd

# Loading order history CSV file
df = pd.read_csv("flipkart_orders.csv")

# Converting order_date into datetime format
df["order_date"] = pd.to_datetime(df["order_date"])

# Extracting year, month and weekday
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["weekday"] = df["order_date"].dt.day_name()

print("Updated Order DataFrame:")
print(df.head())

# Output:
# Displays order_date, year, month and weekday
# for the first 5 orders.