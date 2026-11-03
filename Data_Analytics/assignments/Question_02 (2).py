# Assignment Question


import numpy as np

# Creating an array of daily steps for 10 days
steps = np.array([7500, 8200, 9000, 6500, 10500,
                  7800, 12000, 8500, 6000, 9500])

# Selecting days where steps are greater than 8000
selected_steps = steps[steps > 8000]

print("Daily Steps:", steps)
print("Steps Greater Than 8000:", selected_steps)