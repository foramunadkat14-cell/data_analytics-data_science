# Assignment Question

import pandas as pd

# Creating Instagram posts DataFrame
df = pd.DataFrame({
    "posted_at": [
        "2024-06-01 10:00:00",
        "2024-06-02 12:30:00",
        "2024-06-03 15:45:00",
        "2024-06-04 08:20:00",
        "2024-06-05 18:00:00"
    ]
})

# Converting timestamps into UTC datetime
df["posted_at"] = pd.to_datetime(df["posted_at"], utc=True)

# Converting UTC into Asia/Kolkata timezone
df["posted_at"] = df["posted_at"].dt.tz_convert("Asia/Kolkata")

print("Converted Instagram Post Times:")
print(df.head())

# Output:
# 2024-06-01 15:30:00+05:30
# 2024-06-02 18:00:00+05:30
# 2024-06-03 21:15:00+05:30
# 2024-06-04 13:50:00+05:30
# 2024-06-05 23:30:00+05:30