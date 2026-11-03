# Assignment Question

import pandas as pd

# Creating a list of delivery timestamps
timestamps = [
    "2024-06-01 14:30",
    "2024-06-02 09:15",
    "2024-06-03 20:45"
]

# Converting strings into datetime objects
dates = pd.to_datetime(timestamps)

print("Converted Datetime Values:")
print(dates)

# Output:
# DatetimeIndex:
# 2024-06-01 14:30:00
# 2024-06-02 09:15:00
# 2024-06-03 20:45:00