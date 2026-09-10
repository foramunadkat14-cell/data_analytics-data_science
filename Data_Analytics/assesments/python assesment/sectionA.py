#SCENARIO 1

#You are a data analyst at a food delivery startup. The company has two years of order data sitting in spreadsheets but all decisions are still made by gut feeling. Leadership asks you to map out exactly what steps the team would follow to build a tool that predicts which restaurant zones will face peak demand between 7–9 PM — and they want to know where modern AI tools fit into that process.

#Question 1: Walk through every stage of the Data Science Lifecycle as it applies to this problem. For each stage — Problem Definition, Data Collection, Data Preparation, Exploration, Modelling, and Evaluation — state what concrete deliverable that stage produces. Then identify two specific stages where Generative AI tools could meaningfully accelerate the work, explain the task they would assist with, and describe one risk of relying on AI output without human review at each of those stages.

'''

Answer:

1. Problem Definition:
The goal is to predict which restaurant zones will have peak demand between 7 PM and 9 PM.

Deliverable: A clear problem statement, target variable, required inputs, and success criteria.

2. Data Collection:
Collect two years of order data from spreadsheets, including order time, restaurant zone, number of orders, date, and other useful information.

Deliverable: A complete raw dataset containing historical order records.

3. Data Preparation:
Clean the data by removing duplicates, handling missing values, correcting errors, and converting dates and times into proper formats.

Deliverable: A clean and structured dataset ready for analysis.

4. Exploration:
Analyze the data to identify patterns such as which zones have the highest demand, which days are busiest, and whether weekends have higher demand.

Deliverable: Charts, statistics, and an exploratory data analysis report showing demand patterns.

5. Modelling:
Train a machine-learning model using historical data to predict future demand for each restaurant zone.

Deliverable: A trained prediction model capable of identifying high-demand zones.

6. Evaluation:
Test the model using unseen data and measure its performance using suitable metrics such as MAE or RMSE.

Deliverable: A model evaluation report showing accuracy, errors, and whether the model is suitable for use.

Generative AI in Data Preparation:

Generative AI can help create Python/Pandas code for cleaning data, handling missing values, and removing duplicates.

Risk: AI may generate incorrect cleaning logic and accidentally remove valid records. Therefore, the output must be checked by a human.

Generative AI in Exploration:

Generative AI can help generate SQL/Python code for analyzing the data and creating charts.

Risk: AI may incorrectly interpret a pattern or correlation in the data, which could lead to wrong business decisions. Human review is required.

'''

#SCENARIO 2

#You are collaborating with two other developers on a food delivery project. One teammate is writing the data-cleaning script, another is building the reporting script, and you are building the order-tracking script. Every time any of you pushes code to the main branch, the others' work breaks. Your manager insists the main branch must always be in a working state.


# Question 2 : Explain how a Git branching strategy resolves this coordination problem without slowing the team down. Describe the exact sequence of Git commands each team member would use — from creating their own branch through to raising a Pull Request and completing a reviewed merge. Then describe one realistic merge conflict that could occur in this scenario and how you would resolve it.


'''
Answer:

A Git branching strategy allows each developer to work on a separate branch instead of directly modifying the main branch. This keeps the main branch stable and prevents one developer's unfinished code from breaking another developer's work.

Step 1: Get the latest main branch

Each developer first runs:

git checkout main
git pull origin main

Step 2: Create a separate branch

The developer working on data cleaning creates:

git checkout -b feature/data-cleaning

The reporting developer creates:

git checkout -b feature/reporting

I create a branch for order tracking:

git checkout -b feature/order-tracking

Step 3: Write and commit the code

After completing the work:

git add .
git commit -m "Add order tracking functionality" 

Step 4: Push the branch
git push -u origin feature/order-tracking

Step 5: Create a Pull Request

The developer creates a Pull Request on GitHub from their feature branch to the main branch.

Example:

feature/order-tracking → main
Step 6: Code review

Another developer reviews the code. If changes are requested, the developer makes the changes and commits them:

git add .
git commit -m "Fix review comments"
git push

Step 7: Merge

After the code is approved and tests pass, the Pull Request is merged into main.

The developer can then update their local main branch:

git checkout main
git pull origin main
Example of a merge conflict:

A conflict could happen if the data-cleaning developer and reporting developer both modify the same function in utils.py.

Git may show:

<<<<<<< HEAD
cleaned_data = clean_orders(data)
=======
cleaned_data = prepare_orders(data)
>>>>>>> feature/reporting

The developer checks both changes and decides which code should remain or combines the two changes.

After resolving the conflict:

git add utils.py
git commit -m "Resolve merge conflict"
git push

The Pull Request can then be reviewed and merged.

'''

# SCENARIO 3
# You are a data analyst automating delivery-partner commission payouts for a food delivery startup. The finance team wants the commission applied consistently across a growing list of delivery order records, and manually calculating it in a spreadsheet has started producing errors.


#Question 3 : Design a solution that uses a named function for the calculation logic and applies it across the full list using map() with a lambda. Explain why map() is more appropriate here than writing a second for loop. Then explain what filter() contributes if the finance team needs only the records above a given threshold for an audit, and how functools.reduce() could compute the overall total in a single expression.


'''
Answer:

First, create a named function for calculating commission:

def calculate_commission(amount):
    return amount * 0.10

Suppose the order amounts are:

orders = [500, 800, 1200, 1500]

We can apply the function to every order using map() and lambda:

commission = list(map(lambda amount: calculate_commission(amount), orders))

The result will be:

[50.0, 80.0, 120.0, 150.0]
Why is map() appropriate?

map() is specifically designed to apply the same function to every item in a list. It avoids writing another explicit for loop and makes the purpose of the code clear.

Instead of:

commission = []

for amount in orders:
    commission.append(calculate_commission(amount))

we can use:

commission = list(map(lambda amount: calculate_commission(amount), orders))
filter()

filter() is used when finance needs only records that satisfy a particular condition.

For example, to get orders above ₹1000:

high_value = list(filter(lambda amount: amount > 1000, orders))

Output:

[1200, 1500]
reduce()

reduce() can combine all values into one final value.

from functools import reduce

total = reduce(lambda x, y: x + y, orders)

The total will be:

4000

Therefore:

map() → applies a calculation to every item.
filter() → selects items based on a condition.
reduce() → combines all items into one result.

'''

# SCENARIO 4

# You are designing the account model for a food delivery platform with three types of users — Customer, DeliveryPartner, and Admin — each of which needs to show a different profile summary when display_profile() is called.

#Question 4 : Explain how a base class with inheritance and method overriding cleanly models this. What specific runtime problem occurs if someone writes a loop that iterates over a mixed list of all user objects and calls the display method on each one — when that method is only defined on some subclasses and not on the base class? Then explain how you would redesign the base class so the loop never crashes, regardless of which new subclass is added in future.


'''
Answer:

A base User class can contain common information such as the user's name. The subclasses Customer, DeliveryPartner, and Admin can inherit from the User class.

class User:
    def __init__(self, name):
        self.name = name

Each subclass can override the display_profile() method:

class Customer(User):
    def display_profile(self):
        print("Customer:", self.name)


class DeliveryPartner(User):
    def display_profile(self):
        print("Delivery Partner:", self.name)


class Admin(User):
    def display_profile(self):
        print("Admin:", self.name)

This is called method overriding because each subclass provides its own version of the same method.

If a mixed list contains an object whose class does not have display_profile(), and the base class also does not define it:

for user in users:
    user.display_profile()

Python will raise an:

AttributeError

The loop will stop when it reaches the object that does not contain the method.

Better design:

Define display_profile() in the base class:

class User:
    def __init__(self, name):
        self.name = name

    def display_profile(self):
        print("Generic User:", self.name)

Then subclasses override it:

class Customer(User):
    def display_profile(self):
        print("Customer:", self.name)


class DeliveryPartner(User):
    def display_profile(self):
        print("Delivery Partner:", self.name)


class Admin(User):
    def display_profile(self):
        print("Admin:", self.name)

Now the loop can safely call:

for user in users:
    user.display_profile()

Every subclass inherits the method, so the loop will not crash even if a new subclass is added later.

This is an example of polymorphism.



'''

# SCENARIO 5

# You are integrating a third-party payment gateway API into the food delivery platform's Python backend. During testing, the API intermittently returns status codes 200, 401, 429, and 500 — and one teammate's script crashed and corrupted the output file when the API returned a 500 mid-write.

# Question 5: Explain what each of these status codes means and what the script must do differently in response to each one. Then describe how a try-except-finally block around the file-write step would have prevented the corrupted output file — specifically what finally guarantees and why it runs even when an exception is raised.

'''
Answer:

The API can return four important status codes:

1. Status Code 200 — OK

200 means the API request was successful.

The program should process the returned data normally and save the valid result.

2. Status Code 401 — Unauthorized

401 means the authentication information is invalid, missing, or expired.

The program should check the API key or authentication token and refresh or correct it if possible.

3. Status Code 429 — Too Many Requests

429 means the application has sent too many requests within a certain time.

The program should wait and retry after a delay. A backoff strategy can be used to avoid repeatedly hitting the rate limit.

4. Status Code 500 — Internal Server Error

500 means there is an error on the API server.

The program should treat the request as failed, avoid using incomplete data, log the error, and retry when appropriate.

try-except-finally

A safe file-writing structure is:

file = None

try:
    file = open("output.txt", "w")
    file.write(data)

except Exception as e:
    print("Error:", e)

finally:
    if file:
        file.close()

The try block contains the operation that may produce an error.

The except block handles the error.

The finally block always runs, whether an exception occurs or not.

Therefore, if an exception occurs while writing the file, the finally block still closes the file and releases the file resource.

However, finally itself does not guarantee that a partially written file is never corrupted. A better solution is to write the data to a temporary file first and replace the final file only after the complete write succeeds.


'''

# SCENARIO 6

# You are cleaning a raw customer contact records file where phone numbers were entered inconsistently — some with extra spaces, some with typos, some in completely wrong formats — and the operations team needs a clean list of valid entries before it can be used. 

# Question 6 : Explain how you would use Python's re module to validate and extract only the correctly formatted entries from this text. Describe the general structure of the regular expression pattern you'd use (in words, not just symbols) and explain why re.findall() is more appropriate here than re.search(). Then describe one real-world formatting edge case that a naive pattern would incorrectly reject or accept

'''
Answer:

Python's re module is used for regular expressions, which allow us to search, validate, and extract specific patterns from text.

For Indian mobile numbers, we can create a pattern that checks:

The number contains exactly 10 digits.
The first digit is between 6 and 9.
The remaining nine characters are digits.
There are no unwanted letters or extra characters.  

A suitable basic pattern is:

import re

pattern = r'\b[6-9][0-9]{9}\b'

Suppose the raw data is:

text = """
9876543210
98765 43210
1234567890
987654321
9123456789
"""

We can extract the valid numbers using:

valid_numbers = re.findall(pattern, text)

print(valid_numbers)

Output:

['9876543210', '9123456789']
Why use re.findall()?

re.findall() finds all occurrences that match the pattern.

This is useful because the operations team needs a complete list of valid phone numbers.

On the other hand, re.search() stops after finding the first matching occurrence, so it is not suitable when we need every valid entry.

Real-world edge case:

A naive pattern such as:

r'\d{10}'

may accept:

1234567890

even though an Indian mobile number normally starts with 6, 7, 8, or 9.

Another edge case is:

+91 9876543210

This can be a valid Indian phone number, but a strict 10-digit pattern would reject it because it contains the +91 country code and a space.

Therefore, the regular expression should be designed according to the actual phone-number formats accepted by the company.

'''