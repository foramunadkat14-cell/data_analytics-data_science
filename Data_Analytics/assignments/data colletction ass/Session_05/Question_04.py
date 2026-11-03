# Assignment Question

import pandas as pd
from pathlib import Path

# Creating file paths
base_path = Path(__file__).parent

# Loading CSV files
orders = pd.read_csv(base_path / "orders.csv")
users = pd.read_csv(base_path / "users.csv")

# Merging both DataFrames using user_id
merged_data = pd.merge(
    orders,
    users,
    on="user_id",
    how="inner"
)

print("Combined Orders and Users:")
print(merged_data)

# Output:
# Displays order_id, user_id, amount and username
# for matching user IDs.