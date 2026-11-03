# Assignment Question

import matplotlib.pyplot as plt

# Sample Instagram data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

followers = [100, 150, 180, 220, 250, 300, 350]
posts = [10, 15, 12, 20, 18, 25, 22]

# Creating figure and first axis
fig, ax1 = plt.subplots(figsize=(9, 5))

# First axis: Instagram followers
ax1.plot(
    days,
    followers,
    color="blue",
    marker="o",
    label="Followers"
)

ax1.set_xlabel("Days")
ax1.set_ylabel("Followers", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Creating second axis
ax2 = ax1.twinx()

# Second axis: Daily posts
ax2.bar(
    days,
    posts,
    color="orange",
    alpha=0.5,
    label="Posts"
)

ax2.set_ylabel("Daily Posts", color="orange")
ax2.tick_params(axis="y", labelcolor="orange")

plt.title("Instagram Followers and Daily Posts")

plt.show()

# Output:
# Displays a multi-axis chart showing:
# Blue line: Instagram followers.
# Orange bars: Daily posts.