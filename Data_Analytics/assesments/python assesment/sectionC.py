'''

1. Project Folder Structure

Use the repository you created in Task 1:

food-delivery-pipeline/
│
├── .git/
├── .gitignore
├── README.md
│
├── src/
│   ├── .gitkeep
│   └── food_delivery_pipeline.py
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   │
│   └── processed/
│       ├── .gitkeep
│       └── records.json
│
├── docs/
│   └── .gitkeep
│
└── tests/
    └── .gitkeep
2. Create the Python File

Go inside your repository:

cd food-delivery-pipeline

Create:

src/food_delivery_pipeline.py

Put the following complete code inside it:

import requests
import json


class Order:
    def __init__(self, order_id, name, amount, status):
        self.order_id = order_id
        self.name = name
        self.amount = amount
        self.status = status

    def to_dict(self):
        return {
            "id": self.order_id,
            "name": self.name,
            "amount": self.amount,
            "status": self.status
        }


records = []


API_URL = "https://jsonplaceholder.typicode.com/posts?_limit=10"

FILE_PATH = "data/processed/records.json"


# --------------------------------------------------
# Option 1: Fetch restaurants from API
# --------------------------------------------------

def fetch_restaurants():

    try:
        response = requests.get(API_URL)

        if response.status_code == 200:

            data = response.json()

            print("\nTop 10 Restaurants")
            print("------------------")

            for item in data:

                order = Order(
                    item["id"],
                    item["title"],
                    0.0,
                    False
                )

                records.append(order)

                print(
                    "ID:",
                    order.order_id,
                    "| Name:",
                    order.name
                )

            print("\nRecords fetched successfully.")

        else:
            print(
                "API Error. Status Code:",
                response.status_code
            )

    except requests.RequestException as e:

        print("API request failed:", e)


# --------------------------------------------------
# Option 2: Add a new restaurant
# --------------------------------------------------

def add_restaurant():

    print("\nAdd New Restaurant")
    print("------------------")

    # Validate ID
    while True:

        try:
            order_id = int(input("Enter restaurant ID: "))
            break

        except ValueError:
            print("Invalid input! ID must be a number.")


    name = input("Enter restaurant name: ").strip()


    # Validate amount
    while True:

        try:
            amount = float(input("Enter order amount: "))
            break

        except ValueError:
            print("Invalid input! Amount must be numeric.")


    status_input = input(
        "Is the order delivered? (yes/no): "
    ).strip().lower()


    status = status_input == "yes"


    order = Order(
        order_id,
        name,
        amount,
        status
    )

    records.append(order)

    print("\nRestaurant added successfully.")


# --------------------------------------------------
# Commission calculation
# --------------------------------------------------

def calculate_commission(amount):

    if amount <= 1000:
        return amount * 0.05

    elif amount <= 3000:
        return amount * 0.10

    else:
        return amount * 0.15


def calculate_fees():

    if not records:

        print("\nNo records available.")
        return


    print("\nCommission Details")
    print("-------------------")


    updated_records = list(
        map(
            lambda order: (
                order,
                calculate_commission(order.amount)
            ),
            records
        )
    )


    for order, fee in updated_records:

        print(
            "ID:", order.order_id,
            "| Name:", order.name,
            "| Amount:", order.amount,
            "| Commission:", round(fee, 2)
        )


    threshold = 200


    high_fee_records = list(
        filter(
            lambda item: item[1] > threshold,
            updated_records
        )
    )


    print(
        "\nAudit Records - Commission Above",
        threshold
    )

    print("--------------------------------------")


    if high_fee_records:

        for order, fee in high_fee_records:

            print(
                "ID:", order.order_id,
                "| Name:", order.name,
                "| Commission:", round(fee, 2)
            )

    else:

        print("No records found above the threshold.")


# --------------------------------------------------
# Save records
# --------------------------------------------------

def save_records():

    try:

        with open(FILE_PATH, "w") as file:

            json.dump(
                [record.to_dict() for record in records],
                file,
                indent=4
            )

        print("\nRecords saved successfully.")

    except Exception as e:

        print("Error while saving records:", e)

    finally:

        print("Operation complete.")


# --------------------------------------------------
# Load records
# --------------------------------------------------

def load_records():

    global records

    try:

        with open(FILE_PATH, "r") as file:

            data = json.load(file)


        records = [
            Order(
                item["id"],
                item["name"],
                item["amount"],
                item["status"]
            )
            for item in data
        ]


        print("\nRecords loaded successfully.")

        print("Total records:", len(records))


    except FileNotFoundError:

        print(
            "\nFile not found. Starting with empty records."
        )

        records = []


    except Exception as e:

        print("Error while loading records:", e)


    finally:

        print("Operation complete.")


# --------------------------------------------------
# Display current records
# --------------------------------------------------

def display_records():

    if not records:

        print("\nNo records available.")
        return


    print("\nCurrent Records")
    print("----------------")


    for order in records:

        print(
            "ID:", order.order_id,
            "| Name:", order.name,
            "| Amount:", order.amount,
            "| Delivered:", order.status
        )


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

def main():

    while True:

        print("\n")
        print("==============================")
        print(" FOOD DELIVERY DATA PIPELINE ")
        print("==============================")

        print("1. Fetch and display top 10 restaurants")
        print("2. Add a new restaurant")
        print("3. Calculate commission")
        print("4. Save records")
        print("5. Load records")
        print("6. Display current records")
        print("7. Exit")


        choice = input(
            "\nEnter your choice: "
        ).strip()


        if choice == "1":

            fetch_restaurants()


        elif choice == "2":

            add_restaurant()


        elif choice == "3":

            calculate_fees()


        elif choice == "4":

            save_records()


        elif choice == "5":

            load_records()


        elif choice == "6":

            display_records()


        elif choice == "7":

            print("\nThank you for using the Food Delivery Pipeline.")

            break


        else:

            print(
                "\nInvalid choice! Please select 1-7."
            )


if __name__ == "__main__":

    main()
3. Install requests

Open terminal in the project folder:

python -m pip install requests

Check:

python -m pip show requests
4. Run the Project

From the repository root:

python src/food_delivery_pipeline.py

You should see:

==============================
 FOOD DELIVERY DATA PIPELINE
==============================
1. Fetch and display top 10 restaurants
2. Add a new restaurant
3. Calculate commission
4. Save records
5. Load records
6. Display current records
7. Exit

Enter your choice:
5. Test Option 1 — API Fetch

Enter:

1

The program calls:

https://jsonplaceholder.typicode.com/posts?_limit=10

It checks:

if response.status_code == 200:

before calling:

response.json()

If successful, it converts the API records into Order objects.

The API's:

id

becomes the restaurant ID, and:

title

becomes the restaurant name.

Example:

ID: 1 | Name: sunt aut facere repellat provident occaecati excepturi optio reprehenderit

📸 Take a screenshot showing the 10 records.

6. Test Option 2 — Add Restaurant

Enter:

2

Example:

Enter restaurant ID: 11
Enter restaurant name: Pizza Palace
Enter order amount: 2500
Is the order delivered? (yes/no): yes

Output:

Restaurant added successfully.
Test invalid numeric input

For example:

Enter restaurant ID: abc

The program will show:

Invalid input! ID must be a number.

Then it asks again.

Similarly:

Enter order amount: xyz

gives:

Invalid input! Amount must be numeric.

This satisfies the input validation requirement.

7. Test Option 3 — Commission

Enter:

3

The program uses the named function:

calculate_commission()

with map():

map(
    lambda order: (
        order,
        calculate_commission(order.amount)
    ),
    records
)

The commission tiers are:

Amount <= ₹1000       → 5%
₹1001–₹3000           → 10%
Above ₹3000           → 15%

It also uses filter() to find records where:

Commission > ₹200

Example output:

Commission Details
-------------------
ID: 1 | Name: Swiggy | Amount: 500 | Commission: 25.0
ID: 2 | Name: Zomato | Amount: 2500 | Commission: 250.0

Audit Records - Commission Above 200
--------------------------------------
ID: 2 | Name: Zomato | Commission: 250.0

📸 Take a screenshot.

8. Test Option 4 — Save

Enter:

4

The program creates:

data/processed/records.json

The objects are converted using:

record.to_dict()

and saved using:

json.dump()

Inside the JSON file you will get something similar to:

[
    {
        "id": 1,
        "name": "Swiggy",
        "amount": 500.0,
        "status": true
    },
    {
        "id": 2,
        "name": "Zomato",
        "amount": 2500.0,
        "status": true
    }
]
9. Test Option 5 — Load

First exit and run the program again, or simply choose:

5

It will read:

data/processed/records.json

and recreate the Order class instances.

Output:

Records loaded successfully.
Total records: 11
Operation complete.
10. Git Requirement — At Least 5 Meaningful Commits

This part is very important because the assessment specifically asks for:

At least 5 meaningful commits on the main branch with a feature branch merged in via a Pull Request.

You can use this commit plan.

Commit 1

Your existing Task 1 commit:

git add .
git commit -m "feat: initialise project structure"
Commit 2

Already from Task 1:

git add README.md .gitignore
git commit -m "docs: add README and .gitignore"
Commit 3 — Add capstone base
git add src/food_delivery_pipeline.py
git commit -m "feat: add food delivery pipeline console tool"
Commit 4 — Create feature branch

Create a branch:

git checkout -b feature/json-persistence

Make sure your code contains the save/load functionality.

Then:

git add src/food_delivery_pipeline.py
git commit -m "feat: add JSON persistence"

Push it:

git push -u origin feature/json-persistence
11. Create Pull Request

Go to your GitHub repository.

Create a Pull Request:

feature/json-persistence
            ↓
          main

Add a suitable description such as:

Added JSON save and load functionality for food delivery records.

The feature:
- Saves Order objects to JSON
- Loads records from JSON
- Handles FileNotFoundError
- Handles other exceptions
- Uses finally for operation completion

Get the PR reviewed and merge it.

12. Return to Main

After merging:

git checkout main
git pull origin main

Now the feature branch has been merged into main.

13. Commit 5

Make one additional meaningful improvement, for example improving the README with capstone usage instructions.

Edit README.md and add:

## Mini Capstone

Food Delivery Live Data Pipeline is a console-based Python application that fetches mock restaurant data from a public API, manages records using OOP, calculates commissions using higher-order functions, and persists records using JSON.

### Running the Project

```bash
python src/food_delivery_pipeline.py
Features
Fetch top 10 restaurants from API
Add new restaurant records
Calculate commissions
Save records to JSON
Load records from JSON
Display current records

Then:

```bash
git add README.md
git commit -m "docs: document capstone usage"

Now you have at least 5 meaningful commits.

14. Check Git History

Run:

git log --oneline --graph --all

You want to see something similar to:

* abc1234 docs: document capstone usage
* def5678 feat: add JSON persistence
|\
| * ghi9012 feat: add JSON persistence
|/
* jkl3456 feat: add food delivery pipeline console tool
* mno7890 docs: add README and .gitignore
* pqr1234 feat: initialise project structure

'''