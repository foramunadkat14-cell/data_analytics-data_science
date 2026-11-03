# Assignment Question

import pandas as pd

# Creating Flipkart product reviews
reviews = pd.Series([
    "Good quality",
    "Excellent product",
    "Good quality",
    "Very useful",
    "Good quality",
    "Excellent product",
    "Average product",
    "Excellent product"
])

# Counting repeated reviews
review_counts = reviews.value_counts()

# Displaying top 3 most common reviews
print("Top 3 Most Common Reviews:")
print(review_counts.head(3))

# Output:
# Good quality          3
# Excellent product     3
# Very useful           1