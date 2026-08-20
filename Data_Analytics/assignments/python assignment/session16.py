#1. Use iter() and next() to manually loop through a list of your 5 favorite food delivery apps (like Zomato, Swiggy, Domino's, etc.) and print each app name one by one.

delivery_apps = ["Zomato", "Swiggy", "Domino's", "McDonald's App", "Blinkit"]  
app_iterator = iter(delivery_apps)

print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))


#2. Write a generator function called playlist_generator that takes a list of song names and yields each song one at a time, simulating a Spotify playlist shuffle.

def playlist_generator(songs):
    for song in songs:
        yield song

my_playlist = ["Bohemian Rhapsody", "Shape of You", "Blinding Lights"]
player = playlist_generator(my_playlist)

print(next(player))  
print(next(player)) 
print(next(player))  

#3. Use enumerate() to print out the index and name of each item in a shopping cart list (e.g., ['Pizza', 'Burger', 'Fries', 'Coke']) like Flipkart displays item numbers in your cart.

shopping_cart = ['Cheese Sandwich', 'Pizza', 'Potato Burger', 'Coke']
for index, item in enumerate(shopping_cart, start=1):
    print(f"Item {index}: {item}")

#4. Given two lists — one with cricket team names and one with their IPL points — use zip() to pair each team with its points and print them in the format: 'Team: Mumbai Indians, Points: 18'.

teams = ["Gujarat Titans", "Mumbai Indians", "Chennai Super Kings", "Rajasthan Royals"]
points = [20, 18, 17, 14]
for team, point in zip(teams, points):
    print(f"Team: {team}, Points: {point}")

#5. Create a generator function called order_id_generator that yields a new order ID (starting from 1001) each time it's called, similar to how Zomato or Swiggy generates unique order numbers.<br><br><em><strong>Hint:</strong> Use the yield statement inside a loop to generate the next ID.</em>

def order_id_generator():
    order_id = 1001
    while True:
        yield order_id
        order_id += 1

# Example usage:
get_new_order = order_id_generator()

print(f"New Order Received! ID: {next(get_new_order)}")
print(f"New Order Received! ID: {next(get_new_order)}")
print(f"New Order Received! ID: {next(get_new_order)}")