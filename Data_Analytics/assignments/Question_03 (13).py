# Assignment Question

import pandas as pd

# Loading Zomato restaurant data from TSV file
df = pd.read_csv("zomato_data.tsv", sep="\t")

# Generating summary statistics
summary = df.describe(include="all")

print("Zomato Dataset:")
print(df.head())

print("\nSummary Statistics:")
print(summary)

# Output:
# Displays the first 5 rows of the Zomato dataset.
# Summary Statistics include:
# count, unique, top, freq, mean, std, min, max