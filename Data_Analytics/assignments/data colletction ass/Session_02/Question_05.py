# Assignment Question

import numpy as np

# Creating an array of Spotify song ratings
ratings = np.array([4, -2, 5, -1, 0, 3, -4, 2])

# Replacing all negative ratings with zero
ratings[ratings < 0] = 0

print("Updated Song Ratings:", ratings)

# Output:
# Updated Song Ratings: [4 0 5 0 0 3 0 2]