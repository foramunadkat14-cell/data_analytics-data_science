# Assignment Question

import pandas as pd

# Loading Paytm transactions dataset
df = pd.read_csv("paytm_transactions.csv")

# Calculating 5th and 95th percentiles
lower = df["transaction_amount"].quantile(0.05)
upper = df["transaction_amount"].quantile(0.95)

# Applying Winsorization
df["transaction_amount"] = df["transaction_amount"].clip(
    lower=lower,
    upper=upper
)

# Displaying updated column statistics
print("Updated Transaction Statistics:")
print(df["transaction_amount"].describe())

# Output:
# Displays count, mean, standard deviation,
# minimum, maximum and percentile statistics.