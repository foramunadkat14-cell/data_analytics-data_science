#1. Create a Python class called Product with attributes name and price, and a method get_discounted_price() that returns the price after applying a 10% discount.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 10 / 100)


# Create Product object
product = Product("Shirt", 1000)

# Print discounted price
print("Product Name:", product.name)
print("Discounted Price: Rs.", product.get_discounted_price())


#2. Now create a subclass called Electronics that inherits from Product and overrides the get_discounted_price() method to apply a 20% discount instead of 10%.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 10 / 100)


class Electronics(Product):
    def get_discounted_price(self):
        return self.price - (self.price * 20 / 100)


# Create Electronics object
electronic = Electronics("Headphones", 2000)

# Print discounted price
print("Product Name:", electronic.name)
print("Discounted Price: Rs.", electronic.get_discounted_price())


#3. Write a function show_final_price(item) that takes any Product or Electronics object and prints its name and the discounted price by calling get_discounted_price(). Demonstrate polymorphism by passing both a Product and an Electronics object to this function.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 10 / 100)


class Electronics(Product):
    def get_discounted_price(self):
        return self.price - (self.price * 20 / 100)


def show_final_price(item):
    print("Product Name:", item.name)
    print("Final Price: Rs.", item.get_discounted_price())


# Create objects
product = Product("Shirt", 1000)
electronic = Electronics("Headphones", 2000)

# Demonstrate polymorphism
show_final_price(product)
show_final_price(electronic)


#4. Build a simple Ticket class for a movie booking app with a method get_final_price(). Then, create a subclass PremiumTicket that overrides get_final_price() to add a 50 rupee convenience fee. Show both in action by creating objects and printing their final prices.

# Hint: Use super() in PremiumTicket to reuse the parent method and add the extra fee.

class Ticket:
    def __init__(self, price):
        self.price = price

    def get_final_price(self):
        return self.price


class PremiumTicket(Ticket):
    def get_final_price(self):
        return super().get_final_price() + 50


# Create Ticket objects
normal_ticket = Ticket(200)
premium_ticket = PremiumTicket(200)

# Print final prices
print("Normal Ticket Price: Rs.", normal_ticket.get_final_price())
print("Premium Ticket Price: Rs.", premium_ticket.get_final_price())