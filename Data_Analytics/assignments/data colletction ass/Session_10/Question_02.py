# Assignment Question

import matplotlib.pyplot as plt

# Restaurant names
restaurants = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J"
]

# Zomato ratings
ratings = [4.2, 3.8, 4.5, 3.5, 4.0,
           4.7, 3.9, 4.3, 3.6, 4.8]

# Average meal prices
prices = [250, 180, 400, 150, 300,
          500, 220, 350, 170, 600]

# Creating scatter plot
plt.scatter(ratings, prices)

# Adding restaurant labels
for i, name in enumerate(restaurants):
    plt.annotate(name, (ratings[i], prices[i]))

# Adding title and labels
plt.title("Restaurant Ratings vs Meal Prices")
plt.xlabel("Zomato Ratings")
plt.ylabel("Average Meal Price")

plt.show()

# Output:
# Displays a scatter plot comparing restaurant ratings
# and average meal prices.