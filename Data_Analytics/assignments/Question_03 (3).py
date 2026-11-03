# Assignment Question

import numpy as np

# Creating an array of IPL team scores for 8 matches
ipl_scores = np.array([180, 210, 165, 195, 220, 175, 205, 190])

# Selecting scores from matches 2, 5, and 7 using fancy indexing
selected_scores = ipl_scores[[1, 4, 6]]

print("IPL Scores:", ipl_scores)
print("Scores of Matches 2, 5, and 7:", selected_scores)