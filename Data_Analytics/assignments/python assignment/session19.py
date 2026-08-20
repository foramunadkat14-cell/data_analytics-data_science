#1. Define a Python class called Song with attributes title, artist, and duration (in seconds). Create an object for your favorite song and print its details.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

# Create an object
song1 = Song("Perfect", "Ed Sheeran", 263)

# Print song details
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")


#2. Add a method play_preview(self) to the Song class that prints 'Playing 30-second preview of [title] by [artist]'. Call this method using the object you created.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    # Method to play 30-second preview
    def play_preview(self):
        print("Playing 30-second preview of", self.title, "by", self.artist)

# Create an object
song1 = Song("Perfect", "Ed Sheeran", 263)

# Call the method
song1.play_preview()


#3. Create a class called FoodOrder with attributes: restaurant_name, items (list), and total_price. Write an __init__() constructor to initialize these, then create an object representing your last Zomato or Swiggy order and print its details.

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

# Create a FoodOrder object
order1 = FoodOrder(
    "Domino's",
    ["Pizza", "Garlic Bread"],
    450
)

# Print order details
print("Restaurant:", order1.restaurant_name)
print("Items:", order1.items)
print("Total Price: Rs.", order1.total_price)


#4. Extend the FoodOrder class by adding a method add_item(self, item_name, item_price) that adds the item to the items list and updates total_price. Demonstrate by adding two items to your order and printing the updated total.

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    # Method to add an item
    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.total_price += item_price

# Create an order
order1 = FoodOrder(
    "Domino's",
    ["Pizza", "Garlic Bread"],
    450
)

# Add two items to the order
order1.add_item("Coke", 60)
order1.add_item("Brownie", 100)

# Print updated order details
print("Restaurant:", order1.restaurant_name)
print("Updated Items:", order1.items)
print("Updated Total: Rs.", order1.total_price)


#5. Refactor your Song class so that the duration attribute is optional in the constructor (default to 0 if not provided).

# Hint: Use a default argument for duration in the __init__() method.

class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    # Method to play 30-second preview
    def play_preview(self):
        print("Playing 30-second preview of", self.title, "by", self.artist)

# Duration is not provided, so the default value will be 0
song1 = Song("Perfect", "Ed Sheeran")

# Print song details
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")

# Call the method
song1.play_preview()