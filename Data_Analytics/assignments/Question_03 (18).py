# Assignment Question

import pandas as pd

# Reading JSON data directly from URL
url = "https://jsonplaceholder.typicode.com/users"

df = pd.read_json(url)

# Displaying usernames column
print("Usernames:")
print(df["username"])

# Output:
# Usernames:
# 0                 Bret
# 1            Antonette
# 2             Samantha
# 3             Karianne
# 4               Kamren
# 5      Leopoldo_Corkery
# 6         Elwyn.Skiles
# 7         Maxime_Nienow
# 8             Delphine
# 9        Moriah.Stanton