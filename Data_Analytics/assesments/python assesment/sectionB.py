'''

# TASK 1 — Food Delivery Project Repository Setup

## Step 1: Create the project folder

Open **Git Bash / Terminal** and run:

```bash
mkdir food-delivery-pipeline
cd food-delivery-pipeline
```

## Step 2: Initialise Git

```bash
git init
```

## Step 3: Create folder structure

```bash
mkdir -p src data/raw data/processed docs tests
```

## Step 4: Create `.gitkeep` files

```bash
touch src/.gitkeep
touch data/raw/.gitkeep
touch data/processed/.gitkeep
touch docs/.gitkeep
touch tests/.gitkeep
```

Your structure should now be:

```text
food-delivery-pipeline/
│
├── src/
│   └── .gitkeep
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   └── processed/
│       └── .gitkeep
│
├── docs/
│   └── .gitkeep
│
└── tests/
    └── .gitkeep
```

---

## Step 5: Create `.gitignore`

Create a file named:

```text
.gitignore
```

Put this inside:

```text
venv/
.env

__pycache__/
*.pyc

*.log

config.ini
secrets.json
```

---

## Step 6: Stage and commit

```bash
git add .
git commit -m "feat: initialise project structure"
```

---

# Step 7: Create README.md

Create:

```text
README.md
```

Put this content inside:

```markdown
# Food Delivery Demand Analytics

## Problem Statement

Food delivery companies generate a large amount of order data every day, but making decisions based only on assumptions can lead to inefficient resource planning. This project focuses on analysing food delivery order data to understand demand patterns, identify high-demand restaurant zones, and support better delivery and business decisions.

## Folder Structure

| Folder/File | Description |
|---|---|
| src/ | Source Python code |
| data/raw/ | Raw input data |
| data/processed/ | Cleaned and processed data |
| docs/ | Project documentation |
| tests/ | Test files |
| README.md | Project documentation |
| .gitignore | Files excluded from Git |

## Setup Instructions

1. Clone the repository.
2. Open the project folder in VS Code.
3. Create a Python virtual environment.
4. Activate the virtual environment.
5. Install the required dependencies.
6. Run the Python scripts from the `src/` folder.

## Usage

This section will contain instructions for running the data cleaning, fee calculation, and record management scripts.
```

Then commit it:

```bash
git add README.md .gitignore
git commit -m "docs: add README and .gitignore"
```

---

# Step 8: Test `.gitignore`

Create the log file:

```bash
touch notes.log
```

Create the sample order file:

```bash
touch data/raw/orders_sample.txt
```

Now run:

```bash
git status
```

### What you should see

`notes.log` should **NOT** appear because `.log` files are ignored.

But:

```text
data/raw/orders_sample.txt
```

**should appear as untracked.**

This proves your `.gitignore` is working.

📸 **Take a screenshot of this `git status` output.**

---

# TASK 2 — Food Delivery Record Cleaning Script

Create a file:

```text
task2_cleaning.py
```

Copy this complete code:

```python
# Task 2: Food Delivery Record Cleaning Script

restaurants = [
    "  swiggy  ",
    "ZOMATO",
    "  uber eats",
    "dominos ",
    "  pizza hut  ",
    "",
    "12345",
    "mcdonalds",
    "  subway  ",
    "   "
]

amount_strings = [
    "Rs 150",
    "200.50",
    "Rs 300",
    "450.75",
    "Rs 125",
    "250.25",
    "Rs 500",
    "175.50",
    "Rs 225"
]

clean_restaurants = []
skipped = 0

print("Restaurant Cleaning")
print("-------------------")

for restaurant in restaurants:

    restaurant = restaurant.strip()

    if restaurant == "" or restaurant.isnumeric():
        print("Skipped invalid entry:", restaurant)
        skipped += 1
        continue

    restaurant = restaurant.replace("  ", " ")
    restaurant = restaurant.title()

    clean_restaurants.append(restaurant)
    print("Cleaned:", restaurant)


print("\nAmount Processing")
print("-----------------")

running_total = 0.0

for amount in amount_strings:

    amount = amount.replace("Rs", "").strip()
    amount = float(amount)

    running_total += amount

    print("Amount:", amount)
    print("Running Total:", running_total)


print("\nFinal Summary")
print("-------------")
print("Total valid records:", len(clean_restaurants))
print("Total skipped:", skipped)
print("Running total amount:", round(running_total, 2))
```

### Run it:

```bash
python task2_cleaning.py
```

Take a screenshot showing the output.

### What this demonstrates

* `strip()` → removes extra spaces.
* `replace()` → removes/replaces unwanted text.
* `title()` → standardises restaurant names.
* `isnumeric()` → checks numeric entries.
* `float()` → converts amount strings to numbers.
* `for` loop → processes all records.
* `running_total` → calculates the total amount.

---

# TASK 3 — Food Delivery Fee Calculator

Create:

```text
task3_fee_calculator.py
```

Copy this:

```python
# Task 3: Food Delivery Fee Calculator

from functools import reduce


restaurants = [
    {"id": 1, "name": "Swiggy", "amount": 500},
    {"id": 2, "name": "Zomato", "amount": 1200},
    {"id": 3, "name": "Dominos", "amount": 2500},
    {"id": 4, "name": "Pizza Hut", "amount": 3500},
    {"id": 5, "name": "Subway", "amount": 800},
    {"id": 6, "name": "McDonalds", "amount": 5000}
]


def calculate_commission(amount):
    if amount <= 1000:
        return amount * 0.05

    elif amount <= 3000:
        return amount * 0.10

    else:
        return amount * 0.15


restaurants = list(
    map(
        lambda record: {
            **record,
            "fee": calculate_commission(record["amount"])
        },
        restaurants
    )
)


print("Restaurant Fee Records")
print("----------------------")

for record in restaurants:
    print(record)


threshold = 200

audit_records = list(
    filter(
        lambda record: record["fee"] > threshold,
        restaurants
    )
)


print("\nAudit Records - Fee Above", threshold)
print("-------------------------------------")

for record in audit_records:
    print(record)


total_fee = reduce(
    lambda x, y: x + y,
    map(lambda record: record["fee"], restaurants)
)


print("\nTotal Fee:", round(total_fee, 2))
```

### Run:

```bash
python task3_fee_calculator.py
```

Take a screenshot of the output.

### What you are demonstrating:

**Named function:**

```python
calculate_commission()
```

**3 commission tiers:**

```text
Up to ₹1000       → 5%
₹1001–₹3000       → 10%
Above ₹3000       → 15%
```

**map():**

```python
map(lambda record: ..., restaurants)
```

Calculates the fee for every restaurant.

**filter():**

```python
filter(lambda record: record["fee"] > threshold, restaurants)
```

Finds records whose fee is above the audit threshold.

**reduce():**

```python
reduce(lambda x, y: x + y, ...)
```

Calculates the overall fee in a single expression.

---

# TASK 4 — Food Delivery Record Manager

Now create this file **inside your Task 1 repository**:

```text
src/order_manager.py
```

Use this complete code:

```python
# Task 4: Food Delivery Record Manager with JSON Persistence

import json


class Order:

    def __init__(
        self,
        order_id,
        restaurant_name,
        amount,
        delivery_time_minutes,
        is_delivered
    ):
        self.order_id = order_id
        self.restaurant_name = restaurant_name
        self.amount = amount
        self.delivery_time_minutes = delivery_time_minutes
        self.is_delivered = is_delivered

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "restaurant_name": self.restaurant_name,
            "amount": self.amount,
            "delivery_time_minutes": self.delivery_time_minutes,
            "is_delivered": self.is_delivered
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["order_id"],
            data["restaurant_name"],
            data["amount"],
            data["delivery_time_minutes"],
            data["is_delivered"]
        )


def save_records(records, filepath):

    try:
        with open(filepath, "w") as file:
            json.dump(
                [record.to_dict() for record in records],
                file,
                indent=4
            )

        print("Records saved successfully.")

    except Exception as e:
        print("Error while saving records:", e)

    finally:
        print("Operation complete")


def load_records(filepath):

    try:
        with open(filepath, "r") as file:
            data = json.load(file)

        records = [
            Order.from_dict(record)
            for record in data
        ]

        print("Records loaded successfully.")
        return records

    except FileNotFoundError:
        print("File not found. Returning empty list.")
        return []

    except Exception as e:
        print("Error while loading records:", e)
        return []

    finally:
        print("Operation complete")


# Sample records

records = [
    Order(101, "Swiggy", 450.50, 35, True),
    Order(102, "Zomato", 750.00, 40, True),
    Order(103, "Dominos", 1200.75, 50, False)
]


filepath = "data/processed/records.json"


# Save records

save_records(records, filepath)


# Load records

loaded_records = load_records(filepath)


print("\nLoaded Records")
print("--------------")

for record in loaded_records:
    print(record.to_dict())
```

---

## Run Task 4

Make sure you are in the **root of your repository**:

```bash
cd food-delivery-pipeline
```

Then run:

```bash
python src/order_manager.py
```

You should get output similar to:

```text
Records saved successfully.
Operation complete
Records loaded successfully.
Operation complete

Loaded Records
--------------
{'order_id': 101, 'restaurant_name': 'Swiggy', 'amount': 450.5, 'delivery_time_minutes': 35, 'is_delivered': True}
...
```

A file should also be created:

```text
data/processed/records.json
```

---

# Final Git Commit for Task 4

Check your files:

```bash
git status
```

Then:

```bash
git add src/order_manager.py data/processed/records.json
```

Commit:

```bash
git commit -m "feat: add record manager with JSON persistence"
```

Now check your commit history:

```bash
git log --oneline
```

You should have at least **2 commits**, for example:

```text
abc1234 feat: add record manager with JSON persistence
def5678 docs: add README and .gitignore
ghi9012 feat: initialise project structure
```

📸 **Take a screenshot of `git log --oneline`.**

---

# What You Need to Submit

| Task   | File / Screenshot                                         |
| ------ | --------------------------------------------------------- |
| Task 1 | `.txt` command log + terminal screenshots                 |
| Task 1 | `README.md` + `.gitignore` inside repository              |
| Task 1 | `git status` screenshot                                   |
| Task 2 | `task2_cleaning.py` + output screenshot                   |
| Task 3 | `task3_fee_calculator.py` + output screenshot             |
| Task 4 | `src/order_manager.py` + output screenshot                |
| Task 4 | `git log --oneline` screenshot showing at least 2 commits |

### Your final repository should look approximately like:

```text
food-delivery-pipeline/
│
├── .git/
├── .gitignore
├── README.md
│
├── src/
│   ├── .gitkeep
│   └── order_manager.py
│
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   └── orders_sample.txt
│   │
│   └── processed/
│       ├── .gitkeep
│       └── records.json
│
├── docs/
│   └── .gitkeep
│
├── tests/
│   └── .gitkeep
│
├── task2_cleaning.py
└── task3_fee_calculator.py
```


'''