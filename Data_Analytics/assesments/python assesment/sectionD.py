'''

STEP 1 — BUILD WITH AI
1. Exact Prompt Given to AI

Use this as the prompt you give to ChatGPT:

Write a Python 3 program for a Food Delivery platform with the following requirements:

Fetch the first 5 records from https://jsonplaceholder.typicode.com/posts?_limit=5 and treat them as mock restaurants. Print each record's id and title.
Create a hardcoded list of 6 order amounts.
Apply a tiered commission using a named function, map(), and a lambda:
10% for orders up to Rs 200
15% for orders from Rs 201 to Rs 500
20% for orders above Rs 500
Print each original order amount along with its calculated commission.
Handle an API failure. If the HTTP status code is anything other than 200, print a descriptive error message and stop execution without causing an unhandled exception.
Save the 5 fetched API records to data/processed/records.json using json.dump() inside a with open() context manager. Use indent=2 for readability.

Give me the complete Python code.

STEP 2 — AI's Original Code

You can use the following as the AI-generated original version:

import requests
import json


url = "https://jsonplaceholder.typicode.com/posts?_limit=5"

response = requests.get(url)

if response.status_code != 200:
    print("API Error:", response.status_code)
else:
    data = response.json()

    print("Mock Restaurants")
    print("-----------------")

    for record in data:
        print("ID:", record["id"])
        print("Name:", record["title"])

    amounts = [100, 200, 300, 500, 600, 1000]

    def calculate_commission(amount):
        if amount <= 200:
            return amount * 10 / 100
        elif amount <= 500:
            return amount * 15 / 100
        else:
            return amount * 20 / 100

    commissions = list(
        map(lambda amount: calculate_commission(amount), amounts)
    )

    print("\nCommission Details")
    print("-------------------")

    for amount, commission in zip(amounts, commissions):
        print(
            "Order Amount:",
            amount,
            "Commission:",
            commission
        )

    with open("data/processed/records.json", "w") as file:
        json.dump(data, file, indent=2)

STEP 3 — Test & Debug Without AI

Now you need to say that you tested the AI code yourself and found an issue/improvement.

A good issue to identify is API request failure.

The original code checks the HTTP status code, but requests.get() itself can still fail if there is a network/DNS/connection problem. For example, the internet connection may be unavailable.

So you can improve it by using try-except.

You can also make the API failure handling clearer.

Corrected Version
import requests
import json


url = "https://jsonplaceholder.typicode.com/posts?_limit=5"


try:
    response = requests.get(url)

    if response.status_code != 200:
        print(
            "API request failed. "
            "HTTP Status Code:",
            response.status_code
        )
        exit()

    data = response.json()

except requests.RequestException as e:
    print("Unable to connect to the API:", e)
    exit()


print("Mock Restaurants")
print("-----------------")

for record in data:
    print(
        "ID:",
        record["id"],
        "| Name:",
        record["title"]
    )


amounts = [100, 200, 300, 500, 600, 1000]


def calculate_commission(amount):

    if amount <= 200:
        return amount * 10 / 100

    elif amount <= 500:
        return amount * 15 / 100

    else:
        return amount * 20 / 100


commissions = list(
    map(
        lambda amount: calculate_commission(amount),
        amounts
    )
)


print("\nCommission Details")
print("-------------------")

for amount, commission in zip(amounts, commissions):

    print(
        "Order Amount: Rs",
        amount,
        "| Commission: Rs",
        round(commission, 2)
    )


with open(
    "data/processed/records.json",
    "w"
) as file:

    json.dump(
        data,
        file,
        indent=2
    )


print("\nRecords saved successfully.")
print("File: data/processed/records.json")
STEP 4 — 3–4 Line Debugging Note

This is the note you can submit:

While testing the AI-generated code, I found that it did not handle network or connection errors from requests.get(). If the API could not be reached, the program could raise an exception instead of displaying a clear message. I added a try-except block to handle requests.RequestException and stop the program safely. I also kept the HTTP status check before calling response.json() and verified that the JSON file uses indent=2 and the correct project path.

What to Submit

Your Section D submission should contain these 3 items:

1. Exact AI Prompt

Include the prompt from Step 1.

2. Two versions of code

Clearly label:

AI's Original Code

and

My Corrected Version
3. Testing & Debugging Note

Include the 3–4 line explanation.

One important point

Because the assessment specifically says “working without AI” for Step 2, make sure you actually run the original code, identify/test the issue, and then make the correction yourself. Don't claim you found a bug that you didn't test.


'''