# Assignment Question

import numpy as np

# Creating daily step counts for two friends over 7 days
friend1 = np.array([5000, 7000, 8000, 6500, 9000, 10000, 7500])
friend2 = np.array([6000, 6500, 7500, 7000, 8500, 9500, 8000])

# Element-wise addition
addition = friend1 + friend2

# Element-wise subtraction
subtraction = friend1 - friend2

# Element-wise multiplication
multiplication = friend1 * friend2

# Element-wise division
division = friend1 / friend2

print("Friend 1 Steps:", friend1)
print("Friend 2 Steps:", friend2)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Output:
# Addition: [11000 13500 15500 13500 17500 19500 15500]
# Subtraction: [-1000 500 500 -500 500 500 -500]
# Multiplication: [30000000 45500000 60000000 45500000 76500000 95000000 60000000]
# Division: [0.8333 1.0769 1.0667 0.9286 1.0588 1.0526 0.9375]