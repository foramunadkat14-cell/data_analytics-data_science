#1. Write a lambda function to convert a list of song titles from Spotify to all lowercase letters and use map() to apply it to ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita'], printing the cleaned list.

songs = ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita']
cleaned_songs = list(map(lambda song: song.lower(), songs))
print(cleaned_songs)


#2. Given a list of Zomato restaurant ratings [4.2, 3.8, 4.5, 2.9, 3.5], use filter() with a lambda to find and print only the restaurants with ratings above 4.0.

ratings = [4.2, 3.8, 4.5, 2.9, 3.5]
high_rated = list(filter(lambda rating: rating > 4.0, ratings))
print(high_rated)


#3. Use reduce() from functools to calculate the total price of items in a Flipkart shopping cart: [499, 1299, 299, 799]. Print the final total.<br><br><em><strong>Hint:</strong> Import reduce from functools and use a lambda to sum two numbers.</em>

from functools import reduce
cart_prices = [499, 1299, 299, 799]
total_price = reduce(lambda x, y: x + y, cart_prices)
print(f"Total Cart Price: ₹{total_price}")


#4. Create a function format_followers that takes a number and returns it in 'K' or 'M' format (e.g., 1500 → '1.5K', 1200000 → '1.2M'), then use map() to apply it to a list of follower counts: [950, 1500, 25000, 1200000].

def format_followers(count):
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M".replace('.0M', 'M')
    elif count >= 1_000:
        return f"{count / 1_000:.1f}K".replace('.0K', 'K')
    return str(count)

followers_list = [950, 1500, 25000, 1200000]
formatted_followers = list(map(format_followers, followers_list))
print(formatted_followers)

#5. Use an AI tool like ChatGPT or Copilot to generate a lambda function that filters out all odd numbers from a list of IPL scores [101, 98, 120, 77, 88], then test the code in your Python environment and paste the working code here.

scores = [101, 98, 120, 77, 88]
even_scores = list(filter(lambda x: x % 2 == 0, scores))
print(even_scores)