# Assignment Question

import pandas as pd

# Creating Paytm payment status DataFrame
df = pd.DataFrame({
    "payment_status": [
        " Yes ",
        "yes",
        "Y",
        "No ",
        "no",
        "N",
        " YES "
    ]
})

# Removing extra spaces and converting to lowercase
df["payment_status"] = (
    df["payment_status"].str.strip().str.lower()
)

# Replacing mixed values with standard values
df["payment_status"] = df["payment_status"].replace({
    "yes": 1,
    "y": 1,
    "no": 0,
    "n": 0
})

print("Standardized Payment Status:")
print(df)

# Output:
#    payment_status
# 0               1
# 1               1
# 2               1
# 3               0
# 4               0
# 5               0
# 6               1