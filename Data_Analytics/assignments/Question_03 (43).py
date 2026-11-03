# Assignment Question

import matplotlib.pyplot as plt

# Food delivery platforms
platforms = ["Swiggy", "Zomato", "Dominos"]

# Number of orders
orders = [120, 150, 90]

# Creating bar chart
plt.bar(
    platforms,
    orders,
    color=["blue", "red", "green"],
    label="Orders"
)

# Adding title and labels
plt.title("Food Delivery Orders in Last Month")
plt.xlabel("Platforms")
plt.ylabel("Number of Orders")

# Adding legend
plt.legend()

plt.show()

# Output:
# Displays a bar chart comparing orders
# on Swiggy, Zomato and Dominos.