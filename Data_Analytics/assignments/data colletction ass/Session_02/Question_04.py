import numpy as np

# Creating an array of Flipkart product prices
prices = np.array([1000, 2000, 3000, 4000, 5000])

# Applying 10% discount using broadcasting
discounted_prices = prices * 0.90

print("Original Prices:", prices)
print("Discounted Prices:", discounted_prices)

# Output:
# Original Prices: [1000 2000 3000 4000 5000]
# Discounted Prices: [ 900. 1800. 2700. 3600. 4500.]