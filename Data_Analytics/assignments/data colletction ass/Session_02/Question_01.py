# Assignment Question

import numpy as np

# Creating a 2D array of ratings for 4 users and 5 food items
ratings = np.array([
    [4, 5, 3, 4, 5],
    [5, 4, 4, 3, 5],
    [3, 5, 4, 5, 4],
    [4, 3, 5, 4, 3]
])

print("All Users Ratings:")
print(ratings)

# Extracting ratings of second and third users using slicing
selected_ratings = ratings[1:3, :]

print("Ratings of Second and Third Users:")
print(selected_ratings)