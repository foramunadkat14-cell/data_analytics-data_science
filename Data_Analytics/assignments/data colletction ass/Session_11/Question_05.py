# Assignment Question

import matplotlib.pyplot as plt

# Flipkart monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [100, 150, 130, 180, 250, 200]

# Creating line chart
plt.plot(
    months,
    sales,
    marker="o",
    color="blue",
    linewidth=2
)

# Finding highest sales
max_sales = max(sales)
max_index = sales.index(max_sales)

# Adding custom annotation
plt.annotate(
    "Big Billion Days!",
    xy=(months[max_index], max_sales),
    xytext=(months[max_index], max_sales + 40),
    arrowprops=dict(arrowstyle="->", color="red"),
    color="red",
    fontsize=12
)

# Adding title and labels
plt.title("Flipkart Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()

# Output:
# Displays a line chart of Flipkart monthly sales.
# Highest sales: 250 in May.
# Annotation: Big Billion Days!