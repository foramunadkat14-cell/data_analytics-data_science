# Assignment Question

import matplotlib.pyplot as plt

# Daily steps for the last 7 days
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

steps = [5000, 7000, 6500, 8000, 9000, 11000, 9500]

# Creating line plot
plt.plot(days, steps, marker="o")

# Adding title and labels
plt.title("Daily Steps for 7 Days")
plt.xlabel("Days")
plt.ylabel("Number of Steps")

# Rotating x-axis labels
plt.xticks(rotation=45)

# Saving chart as PNG file
plt.tight_layout()
plt.savefig("steps_lineplot.png")

# Displaying chart
plt.show()

# Output:
# Displays a line chart showing daily steps for 7 days.
# Chart saved as steps_lineplot.png