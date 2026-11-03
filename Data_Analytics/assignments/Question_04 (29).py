# Assignment Question

import pandas as pd

# Creating Flipkart product price DataFrame
df = pd.DataFrame({
    "product": ["Mobile", "Laptop", "Headphones", "Watch"],
    "price": ["₹12,999", "₹55,999", "₹1,499", "₹2,999"]
})

# Removing currency symbols and commas
df["price"] = df["price"].str.replace(
    r"[₹,]", "", regex=True
)

# Converting price column into numeric type
df["price"] = df["price"].astype(float)

print("Updated Product Prices:")
print(df)

print("\nData Types:")
print(df.dtypes)

# Output:
#       product    price
# 0      Mobile  12999.0
# 1      Laptop  55999.0
# 2  Headphones   1499.0
# 3       Watch   2999.0
#
# product     object
# price      float64