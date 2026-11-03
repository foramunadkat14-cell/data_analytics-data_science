# Assignment Question

import matplotlib.pyplot as plt

# Creating Instagram data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Daily screen time in hours
screen_time = [2, 3, 2.5, 4, 3.5, 5, 4.5]

# Number of posts liked each day
likes = [20, 35, 25, 40, 30, 50, 45]

# Creating figure with two subplots
plt.figure(figsize=(10, 5))

# First subplot: Line plot
plt.subplot(1, 2, 1)

plt.plot(days, screen_time, marker="o", color="blue")

plt.title("Daily Instagram Screen Time")
plt.xlabel("Days")
plt.ylabel("Screen Time (Hours)")

# Second subplot: Bar chart
plt.subplot(1, 2, 2)

plt.bar(days, likes, color="orange")

plt.title("Daily Instagram Likes")
plt.xlabel("Days")
plt.ylabel("Number of Likes")

# Adjusting layout
plt.tight_layout()

# Saving figure
plt.savefig("social_media_usage.png")

# Displaying figure
plt.show()

# Output:
# Displays two plots:
# 1. Line plot showing daily Instagram screen time.
# 2. Bar chart showing daily Instagram likes.
#
# Figure saved as social_media_usage.png