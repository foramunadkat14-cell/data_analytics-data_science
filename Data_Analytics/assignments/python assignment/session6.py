# 1. Create a Python dictionary called insta_followers that stores the number of followers for 5 Instagram influencers (use their usernames as keys and follower counts as values). Print the dictionary.

insta_followers = { "viratkohli": 271000000,"shraddhakapoor": 95000000,"aliaabhatt": 87000000,"narendramodi": 105000000,"deepikapadukone": 81000000 }
print(insta_followers)

# 2. Add a new influencer to your insta_followers dictionary and update the follower count for one existing influencer. Then, delete one influencer from the dictionary and print the updated dictionary.

# Add influencer
insta_followers["kiara_advani"] = 40000000

# Update influencer's follower count
insta_followers["aliaabhatt"] = 88000000

# Delete 1 influencer
del insta_followers["deepikapadukone"]
print(insta_followers)


# 3. Given a dictionary called food_prices with 5 Zomato food items as keys and their prices as values, write code to display all items that cost more than ₹200.

food_prices = { "Pizza": 299,"Burger": 180,"Pasta": 250,"Biryani": 220,"Sandwich": 150 }
for item, price in food_prices.items():
    if price > 200:
        print(item, ":", price)


# 4. Create two sets: flipkart_users and myntra_users, each containing 5 unique usernames. Find and print the set of users who have accounts on both platforms using set intersection.

flipkart_users = {"foram", "astha", "faiz", "mishri", "pranav"}
myntra_users = {"astha", "faiz", "riya", "rahul", "foram"}
common_users = flipkart_users.intersection(myntra_users)
print(common_users)

# 5. Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) that takes two sets of artist names and returns a set of all unique artists across both playlists (set union).<br><br><em><strong>Hint:</strong> Use the union() method or the | operator for sets.</em>

def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)
playlist1 = {"Arijit Singh", "Shreya Ghoshal", "Atif Aslam"}
playlist2 = {"Arijit Singh", "Neha Kakkar", "Diljit Dosanjh"}
result = get_unique_artists(playlist1, playlist2)
print(result)