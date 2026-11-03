# Assignment Question

import pandas as pd

# Loading Paytm transaction data from semicolon-separated CSV
df = pd.read_csv("paytm_transactions.csv", sep=";")

# Checking missing values in each column
missing_values = df.isnull().sum()

print("Missing Values in Each Column:")
print(missing_values)

# Displaying columns containing missing values
print("\nColumns with Missing Values:")

print(missing_values[missing_values > 0])

# Output:
# Missing Values in Each Column:
# Transaction_ID    0
# Customer_Name     2
# Amount             1
# Payment_Mode       0
#
# Columns with Missing Values:
# Customer_Name    2
# Amount           1