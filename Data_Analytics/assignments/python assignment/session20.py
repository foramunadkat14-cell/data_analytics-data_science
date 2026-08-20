#1. Create a Python class called Playlist with a private attribute _songs (a list) and a public method add_song(song) to add a song title to the playlist. Print the playlist after adding 3 songs.

class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)


# Create Playlist object
playlist = Playlist()

# Add 3 songs
playlist.add_song("Perfect")
playlist.add_song("Shape of You")
playlist.add_song("Believer")

# Print the playlist
print("Playlist:", playlist._songs)


#2. Build a Product class for a Flipkart-style app with a private attribute _price. Implement get_price() and set_price() methods to access and update the price. Demonstrate setting and getting the price for a product object.

class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price


# Create Product object
product = Product(15000)

# Get the price
print("Original Price:", product.get_price())

# Set a new price
product.set_price(12000)

# Get the updated price
print("Updated Price:", product.get_price())


#3. Create a Movie class with a private attribute _rating (float between 0 and 10). Write getter and setter methods for _rating. The setter should only allow values between 0 and 10; if an invalid value is given, print an error message.

# Constraint: Do not allow direct access to _rating outside the class.

class Movie:
    def __init__(self, rating):
        self._rating = 0
        self.set_rating(rating)

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self._rating = rating
        else:
            print("Error: Rating must be between 0 and 10.")


# Create Movie object
movie = Movie(8.5)

# Get the rating
print("Movie Rating:", movie.get_rating())

# Try to set an invalid rating
movie.set_rating(12)

# Get the rating again
print("Movie Rating:", movie.get_rating())


#4. Design a simple abstract class PaymentMethod with an abstract method pay(amount). Then, create two subclasses: Paytm and PhonePe, each implementing pay(amount) to print a different message. Instantiate both and call their pay methods with any amount.

from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class Paytm(PaymentMethod):
    def pay(self, amount):
        print("Payment of Rs.", amount, "made using Paytm.")


class PhonePe(PaymentMethod):
    def pay(self, amount):
        print("Payment of Rs.", amount, "made using PhonePe.")


# Create objects
paytm = Paytm()
phonepe = PhonePe()

# Call pay methods
paytm.pay(500)
phonepe.pay(750)