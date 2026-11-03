# Assignment Question

import pandas as pd

# Creating mock Zomato order history dataset
data = {
    "restaurant_name": ["Dominos", "McDonalds", "KFC", "Dominos", "KFC"],
    "order_date": ["2026-10-01", "2026-10-02", "2026-10-03",
                   "2026-10-01", "2026-10-03"]
}

df = pd.DataFrame(data)

# Detecting duplicate orders
duplicates = df.duplicated(
    subset=["restaurant_name", "order_date"]
)

print("Duplicate Orders:")
print(df[duplicates])

# Output:
# Duplicate Orders:
#   restaurant_name  order_date
# 3         Dominos  2026-10-01
# 4             KFC  2026-10-03