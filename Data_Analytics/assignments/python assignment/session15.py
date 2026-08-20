#1. Write a Python function called get_song_duration_per_minute that divides the total duration of a Spotify playlist (in minutes) by the number of songs, and handles the case where the number of songs is zero using try, except, and finally blocks.

def get_song_duration_per_minute(total_duration, num_songs):
    try:
        average_duration = total_duration / num_songs
        print(f"Average song duration: {average_duration:.2f} minutes")
        return average_duration
    except ZeroDivisionError:
        print("Error: The playlist has no songs (cannot divide by zero).")
        return 0
    finally:
        print("Spotify playlist calculation attempt complete.\n")


#2. Build a Flipkart-style price-per-item calculator: take total cart amount and item count as input, perform division, and use try-except to catch and display a user-friendly message if the item count is zero.

def flipkart_price_calculator(total_cart_amount, item_count):
    try:
        price_per_item = total_cart_amount / item_count
        print(f"Your price per item is: ₹{price_per_item:.2f}")
        return price_per_item
    except ZeroDivisionError:
        print("Oops! It looks like your cart is empty. Please add items to calculate the price.")
        return None


#3. Create a Paytm cashback calculator that asks for total spend and number of offers applied, then divides spend by offers to show average cashback per offer. If the number of offers is zero, raise a custom exception called NoOffersApplied and display a custom error message.<br><br><em><strong>Hint:</strong> Define your own exception class by subclassing Exception.</em>

class NoOffersApplied(Exception):
    pass

def calculate_paytm_cashback(total_spend, num_offers):
    try:
        if num_offers == 0:
            raise NoOffersApplied("No offers applied. Add at least one promo code to see average spend per offer.")
        
        average_spend_per_offer = total_spend / num_offers
        print(f"Average spend per offer applied: ₹{average_spend_per_offer:.2f}")
        return average_spend_per_offer
        
    except NoOffersApplied as e:
        print(f"Paytm Error: {e}")
        return None


#4. Refactor the following buggy code to handle exceptions correctly so it never crashes and always prints 'Thank you for using the calculator' at the end, even if an exception occurs:<br><br>def calculate_average_rating(total_rating, num_reviews):<br> return total_rating / num_reviews<br>print(calculate_average_rating(500, 0))

def calculate_average_rating(total_rating, num_reviews):
    try:
        average = total_rating / num_reviews
        return average
    except ZeroDivisionError:
        return "No reviews yet. Cannot calculate average rating."
    finally:
        print("Thank you for using the calculator")


#5. Write a function called safe_divide_for_zomato that takes two numbers (bill amount and number of people), uses try, except, else, and finally to divide the bill and print the result, print a custom error if division by zero, and always print 'Split calculation done' at the end.

def safe_divide_for_zomato(bill_amount, num_people):
    try:
        per_person = bill_amount / num_people
    except ZeroDivisionError:
        print("Zomato split error: You cannot split a bill with zero people!")
    else:
        print(f"Success! Each person needs to pay: ₹{per_person:.2f}")
    finally:
        print("Split calculation done\n")
