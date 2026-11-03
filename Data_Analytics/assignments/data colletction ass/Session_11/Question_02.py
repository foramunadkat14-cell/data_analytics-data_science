# Assignment Question

import matplotlib.pyplot as plt

# Delivery platforms
platforms = ["Zomato", "Swiggy", "Dominos"]

# Average delivery times in minutes
delivery_times = [30, 25, 35]

# Creating bar chart
plt.bar(
    platforms,
    delivery_times,
    color=["red", "orange", "blue"],
    edgecolor="black",
    linewidth=2
)

# Adding title and labels
plt.title("Average Delivery Time Comparison")
plt.xlabel("Delivery Platforms")
plt.ylabel("Delivery Time (Minutes)")

plt.show()

# Output:
# Zomato: 30 minutes
# Swiggy: 25 minutes
# Dominos: 35 minutes
# Displays a bar chart comparing delivery times.