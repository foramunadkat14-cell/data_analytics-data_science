# Assignment Question

import numpy as np

# Creating a 3x3 matrix
matrix = np.array([
    [4, 2, 1],
    [2, 5, 3],
    [1, 3, 6]
])

# Calculating inverse
inverse = np.linalg.inv(matrix)

# Calculating determinant
determinant = np.linalg.det(matrix)

# Calculating eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Original Matrix:")
print(matrix)

print("Inverse Matrix:")
print(inverse)

print("Determinant:", determinant)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

# Output:
# Determinant: 67.0
#
# Eigenvalues:
# [9.3485 3.7302 1.9213]
#
# The inverse matrix exists because the determinant is non-zero.