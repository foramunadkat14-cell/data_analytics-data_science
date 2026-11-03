# Assignment Question

import matplotlib.pyplot as plt

# Spotify listening session durations in minutes
durations = [
    15, 20, 25, 30, 35,
    40, 45, 50, 55, 60,
    22, 28, 33, 38, 42,
    48, 52, 58, 65, 70
]

# Creating histogram with 5 bins
plt.hist(
    durations,
    bins=5,
    color="purple",
    edgecolor="black"
)

# Adding title and labels
plt.title("Spotify Listening Session Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Frequency")

plt.show()

# Output:
# Displays a histogram showing the frequency
# of Spotify listening session durations.