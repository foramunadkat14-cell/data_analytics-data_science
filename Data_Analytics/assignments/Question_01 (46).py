# Assignment Question

import matplotlib.pyplot as plt

# Sample data
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [100, 150, 120, 180, 200]
ratings = [3, 4, 5, 4, 5]

# Creating 2x2 grid of subplots
fig, ax = plt.subplots(2, 2, figsize=(10, 7))

# Line chart
ax[0, 0].plot(days, sales, color="blue", marker="o")
ax[0, 0].set_title("Line Chart")

# Bar chart
ax[0, 1].bar(days, sales, color="green")
ax[0, 1].set_title("Bar Chart")

# Scatter plot
ax[1, 0].scatter(days, ratings, color="red")
ax[1, 0].set_title("Scatter Plot")

# Pie chart
ax[1, 1].pie(
    sales,
    labels=days,
    autopct="%1.1f%%"
)
ax[1, 1].set_title("Pie Chart")

plt.tight_layout()
plt.show()

# Output:
# Displays four charts in a 2x2 grid:
# Line chart, Bar chart, Scatter plot and Pie chart.