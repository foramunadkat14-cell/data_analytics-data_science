# 1. Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, and print the list.

playlist_ids = [101, 205, 309, 412, 587]
print(playlist_ids)


# 2. Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list.<br><br><em><strong>Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>

playlist_ids = [101, 205, 309, 412, 587]
playlist_ids.append(690)
playlist_ids.extend([721, 845])
print(playlist_ids)

# 3. Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist.

playlist_ids = [101, 205, 309, 412, 587, 690, 721, 845]
removed_song = playlist_ids.pop()
print("Removed Song ID:", removed_song)
print("Remaining Playlist:", playlist_ids)


# 4. Create a tuple called insta_filters with 4 Instagram filter names (as strings). Try to change the first filter name and observe what error you get.<br><br><em><strong>Hint:</strong> Tuples are immutable. Note down the error message.</em>

insta_filters = ("Clarendon", "Juno", "Lark", "Gingham")
insta_filters[0] = "Valencia"
print(insta_filters)

# 5. Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) and prints which one should use a list and which should use a tuple, explaining your choice in a comment.


recent_orders = ["Pizza", "Burger", "Biryani"]
ipl_teams = ("MI", "CSK", "RCB", "KKR", "GT", "RR", "LSG", "SRH", "PBKS", "DC")
print("Recent Orders (List):", recent_orders)
print("IPL Teams (Tuple):", ipl_teams)

# Explanation:
# Use a list for recent Zomato orders because orders can be added or removed.
# Use a tuple for IPL team names because they are fixed and should not be changed.