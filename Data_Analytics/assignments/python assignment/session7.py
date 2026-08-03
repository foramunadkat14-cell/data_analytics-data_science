# 1. Write a Python script that takes your current Spotify listening time in minutes and checks if it is above 120 minutes; if yes, print 'You are a true music fan!', otherwise print 'Keep listening!'.

listening_time = int(input("Enter your Spotify listening time (in minutes): "))
if listening_time > 120:
    print("You are a true music fan!")
else:
    print("Keep listening!")

# 2. Create a Python program that asks the user to enter their Zomato order amount and checks if it is above 300; if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.

order_amount = float(input("Enter your Zomato order amount: ₹"))
if order_amount > 300:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")

# 3. Build a Python script that takes your Flipkart cart total and applies the following logic: if total > 2000, print 'You get a 10% discount'; elif total > 1000, print 'You get a 5% discount'; else print 'No discount available'.

cart_total = float(input("Enter your Flipkart cart total: "))
if cart_total > 2000:
    print("You get a 10% discount")
elif cart_total > 1000:
    print("You get a 5% discount")
else:
    print("No discount available")


# 4. Write a Python program that asks the user to enter their IPL fantasy team points and uses nested if-else statements to print: 'Champion' if points > 800, 'Top Performer' if points between 500 and 800, 'Keep Trying' otherwise.<br><br><em><strong>Hint:</strong> Use nested if-else blocks to check the ranges.</em>

points = int(input("Enter your IPL fantasy team points: "))
if points > 500:
    if points > 800:
        print("Champion")
    else:
        print("Top Performer")
else:
    print("Keep Trying")