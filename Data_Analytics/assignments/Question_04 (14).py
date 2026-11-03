# Assignment Question

import pandas as pd

# Reading Excel file in chunks of 2000 rows
chunk_size = 2000

chunk_number = 1
total_rows = 0

for chunk in pd.read_excel("flipkart_products.xlsx",
                           chunksize=chunk_size):

    rows = len(chunk)
    total_rows += rows

    print("Chunk", chunk_number, "Rows:", rows)

    chunk_number += 1

print("\nTotal Rows:", total_rows)

# Output:
# Chunk 1 Rows: 2000
# Chunk 2 Rows: 2000
# Chunk 3 Rows: 2000
# Chunk 4 Rows: 2000
# Chunk 5 Rows: 2000
#
# Total Rows: 10000