#1. Use re.findall() to extract all valid phone numbers from a given string in the format '+91-XXXXXXXXXX' (e.g., '+91-9876543210'). Print the list of found numbers.

import re

text = "Please contact support at +91-9876543210 or our alternate number +91-1234567890. Invalid: +91-12345."

# \+91- matches the exact prefix (escaping the +)
# \d{10} matches exactly 10 digits
pattern = r"\+91-\d{10}"
phone_numbers = re.findall(pattern, text)

print("Found phone numbers:", phone_numbers)

#2. Write a Python function using re.search() that checks if a string contains a valid date in the format 'DD/MM/YYYY'. The function should return True if a date is found, otherwise False.

import re

def contains_date(text):
    # \b ensures word boundaries so it doesn't match inside longer number strings
    # \d{2} matches two digits, \d{4} matches four digits
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    
    if re.search(pattern, text):
        return True
    return False

# Example usage:
print(contains_date("My birthday is on 15/08/2026.")) # Returns True
print(contains_date("The deadline is tomorrow."))     # Returns False

#3. Given a block of text containing multiple prices (like 'Rs. 299', 'Rs. 1500', etc.), use re.findall() to extract all the numeric price values as integers and print their sum.<br><br><em><strong>Hint:</strong> Look for patterns like 'Rs. ' followed by one or more digits.</em>

import re

text = "Your order includes a shirt for Rs. 299, a jacket for Rs. 1500, and socks for Rs. 50."

# Rs\. matches 'Rs.' literally, followed by a space
# (\d+) captures one or more digits into a group
pattern = r"Rs\. (\d+)"
prices_str = re.findall(pattern, text)

# Convert extracted strings to integers and sum them
total_sum = sum(int(price) for price in prices_str)

print("Extracted prices:", prices_str)
print("Total Sum: Rs.", total_sum)

#4. Use re.sub() to replace all email addresses in a string with '[hidden email]' and print the modified string.<br><br><em><strong>Constraint:</strong> Do not use any external libraries except re.</em>

import re

text = "Send your resume to hr@company.com or reach out to admin_123@domain.org for queries."

# Standard email regex pattern
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

redacted_text = re.sub(pattern, "[hidden email]", text)

print(redacted_text)

#5. Download a sample Instagram comments text file (or create your own with at least 10 lines), then write a Python script to extract all valid Instagram usernames (pattern: starts with '@', followed by letters, numbers, underscores, minimum 3 characters) using re.findall() and print the unique usernames.

import re

# Simulated Instagram comments text
comments_text = """
Great picture! @john_doe
Where was this taken? @traveler_99
Loved it! @john_doe
Too short @ab
Check this out @python_coder_2026!
"""

# @ matches the literal '@'
# [a-zA-Z0-9_]{3,} matches letters, numbers, and underscores, minimum 3 times
pattern = r"@[a-zA-Z0-9_]{3,}"

# findall() gets all matches, set() removes duplicates, list() converts back to a list
usernames = list(set(re.findall(pattern, comments_text)))

print("Unique Instagram Usernames:")
for user in usernames:
    print(user) 