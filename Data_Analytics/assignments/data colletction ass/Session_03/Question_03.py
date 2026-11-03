# Assignment Question

import numpy as np

# Creating a 4x4 matrix representing pixel brightness
image = np.array([
    [120, 150, 180, 200],
    [100, 130, 160, 190],
    [80, 110, 140, 170],
    [60, 90, 120, 150]
])

# Transposing the matrix
transposed_image = image.T

# Calculating statistical values
mean_value = np.mean(image)
median_value = np.median(image)
std_value = np.std(image)
variance_value = np.var(image)

print("Original Image:")
print(image)

print("Transposed Image:")
print(transposed_image)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)
print("Variance:", variance_value)

# Output:
# Transposed Image:
# [[120 100  80  60]
#  [150 130 110  90]
#  [180 160 140 120]
#  [200 190 170 150]]

# Mean: 134.375
# Median: 135.0
# Standard Deviation: 39.2059
# Variance: 1537.1093