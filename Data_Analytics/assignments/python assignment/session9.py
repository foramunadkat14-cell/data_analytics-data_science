# 1. Define a function called calculate_final_price(price, discount_rate) that returns the final price after applying the discount rate to the given price.

def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate / 100)
    return final_price


# 2. Create a function called get_delivery_charge(amount, city='Ahmedabad') that returns 0 if city is 'Ahmedabad', otherwise returns 50 as a delivery charge.<br><br><em><strong>Hint:</strong> Use a default argument for the city parameter.</em>

def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 0
    else:
        return 50


# 3. Write a function called format_price(price, currency='INR') that returns a string like '₹500' if currency is 'INR', or '$500' if currency is 'USD'.

def format_price(price, currency="INR"):
    if currency == "INR":
        return f"₹{price}"
    else:
        return f"${price}"

# 4. Build a function called apply_coupon(price, coupon_code=None) that returns the price after a 10% discount if coupon_code is 'ZOMATO10', otherwise returns the original price.<br><br><em><strong>Constraint:</strong> Use a default argument for coupon_code.</em>

def apply_coupon(price, coupon_code=None):
    if coupon_code == "ZOMATO10":
        return price - (price * 10 / 100)
    else:
        return price
