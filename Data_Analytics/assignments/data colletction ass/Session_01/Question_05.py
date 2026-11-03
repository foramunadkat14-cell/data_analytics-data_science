# Assignment Question

import numpy as np

# Creating a Python list of cricket scores
scores = [45, 67, 120, 89, 54]

# Converting the list into a NumPy array
cricket_scores = np.array(scores)

print("Cricket Scores:", cricket_scores)
print("Memory Size of Each Score:", cricket_scores.itemsize, "bytes")


#output

# Cricket Scores: [ 45  67 120  89  54]
# Memory Size of Each Score: 8 bytes