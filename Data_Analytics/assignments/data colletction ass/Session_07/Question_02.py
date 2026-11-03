# Assignment Question

import pandas as pd
import matplotlib.pyplot as plt

# Loading Swiggy orders dataset
df = pd.read_csv("swiggy_orders.csv")

# Creating boxplot
plt.boxplot(df["order_amount"])

# Adding labels and title
plt.title("Swiggy Order Amount Outliers")
plt.xlabel("Orders")
plt.ylabel("Order Amount")

# Displaying boxplot
plt.show()

# Output:
# Displays a boxplot showing the distribution
# of order amounts and any potential outliers.