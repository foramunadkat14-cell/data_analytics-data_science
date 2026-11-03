# Assignment Question

import numpy as np

# Creating two 3x3 matrices
user_preferences = np.array([
    [5, 2, 3],
    [1, 4, 2],
    [3, 2, 5]
])

song_popularity = np.array([
    [4, 1, 2],
    [2, 5, 1],
    [1, 3, 4]
])

# Calculating recommendation matrix using dot()
dot_result = np.dot(user_preferences, song_popularity)

# Calculating recommendation matrix using matmul()
matmul_result = np.matmul(user_preferences, song_popularity)

print("Dot Product Result:")
print(dot_result)

print("Matrix Multiplication Result:")
print(matmul_result)

# Output:
# Dot Product Result:
# [[27 24 24]
#  [14 27 14]
#  [21 28 28]]

# Matrix Multiplication Result:
# [[27 24 24]
#  [14 27 14]
#  [21 28 28]]

# Explanation:
# Both np.dot() and np.matmul() produce the same result
# for two-dimensional matrices.
# np.matmul() is specifically designed for matrix multiplication.