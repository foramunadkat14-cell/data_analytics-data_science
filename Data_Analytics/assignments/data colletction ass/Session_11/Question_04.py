# Assignment Question

import matplotlib.pyplot as plt

# Bollywood movie names
movies = [
    "Movie A",
    "Movie B",
    "Movie C",
    "Movie D",
    "Movie E"
]

# Number of tickets sold (in thousands)
tickets = [50, 80, 65, 100, 90]

# IMDb ratings
ratings = [7.5, 8.2, 6.9, 8.8, 7.8]

# Creating scatter plot
plt.scatter(
    tickets,
    ratings,
    color="purple",
    marker="o",
    s=100
)

# Adding movie names as annotations
for i, movie in enumerate(movies):
    plt.annotate(
        movie,
        (tickets[i], ratings[i]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )

# Adding title and labels
plt.title("Movie Tickets Sold vs IMDb Ratings")
plt.xlabel("Tickets Sold (Thousands)")
plt.ylabel("IMDb Ratings")

plt.show()

# Output:
# Displays a scatter plot comparing movie ticket sales
# and IMDb ratings with movie names above each point.