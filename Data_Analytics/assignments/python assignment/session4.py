# 1. Take the string 'Flipkart-Sale2024' and use string methods to convert it to lowercase, replace the dash with a space, and print the result.

text = "Flipkart-Sale2024"
result = text.lower().replace("-", " ")
print(result)


# 2. Given the product name ' OnePlus Nord-CE 3 ', write code to clean it by removing extra spaces, converting all letters to uppercase, and replacing the dash with a colon.<br><br><em><strong>Hint:</strong> Use strip(), upper(), and replace() methods in sequence.</em>


product = " OnePlus Nord-CE 3 "
clean_product = product.strip().upper().replace("-", ":")
print(clean_product)


# 3. Write a function split_product_code(product_code) that takes a string like 'ZOMATO-FOOD-2024' and returns a list of its parts using the split() method.


def split_product_code(product_code):
    return product_code.split("-")
code = "ZOMATO-FOOD-2024"
print(split_product_code(code))


# 4. Given the string 'Spotify_Premium_Offer', use string slicing to extract and print only the word 'Premium'.

text = "Spotify_Premium_Offer"
print(text[8:15])


# 5. Format and print a message using variables: product = 'Myntra Shirt', price = 799.5. The output should be: 'Deal: Myntra Shirt is available at ₹799.50 only!' using string formatting.

product = "Myntra Shirt"
price = 799.5
print(f"Deal: {product} is available at ₹{price:.2f} only!")
