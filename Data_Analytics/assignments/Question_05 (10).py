# Assignment Question

import numpy as np

# Creating a NumPy array of shape (2, 6)
orders = np.array([
    [10, 12, 15, 14, 18, 20],
    [8, 11, 13, 16, 17, 19]
])

# Reshaping array into (3, 4)
reshaped = orders.reshape(3, 4)

# Flattening the array
flattened = orders.flatten()

# Splitting array into two equal parts
split_array = np.array_split(flattened, 2)

# Stacking both parts vertically
stacked = np.vstack(split_array)

print("Original Array:")
print(orders)

print("Reshaped Array:")
print(reshaped)

print("Flattened Array:")
print(flattened)

print("First Part:")
print(split_array[0])

print("Second Part:")
print(split_array[1])

print("Vertically Stacked Array:")
print(stacked)

# Output:
# Reshaped Array:
# [[10 12 15 14]
#  [18 20  8 11]
#  [13 16 17 19]]

# Flattened Array:
# [10 12 15 14 18 20 8 11 13 16 17 19]

# First Part:
# [10 12 15 14 18 20]

# Second Part:
# [ 8 11 13 16 17 19]

# Vertically Stacked Array:
# [[10 12 15 14 18 20]
#  [ 8 11 13 16 17 19]]