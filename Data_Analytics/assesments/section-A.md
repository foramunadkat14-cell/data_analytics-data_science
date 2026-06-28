# Section A: Concept Application

1. You are setting up a new database for the Zomato project. Which SQL
command creates a new database called analytics_db?

```
CREATE DATABASE analytics_db;
```

2. You add a restaurant_id column to the restaurants table as its primary key.
What is a primary key, and why must its values be unique?

```
A Primary Key is a column (or group of columns) that uniquely identifies every record in a table.

example: restaurant_id INT PRIMARY KEY

It must be unique because:

No two records should have the same ID.
It prevents duplicate entries.
It allows tables to be linked accurately.

```

3. The ratings table references restaurant_id from the restaurants table. What is
a foreign key, and what integrity rule does it enforce?

```
A Foreign Key is a column that references the Primary Key of another table.

example: 

restaurant_id INT,
FOREIGN KEY (restaurant_id)
REFERENCES restaurants(restaurant_id)

```

4. You apply a NOT NULL constraint to the restaurant_name column. What kind of
data entry does this constraint prevent?

```
restaurant_name VARCHAR(255) NOT NULL
```

5. You draw an ER diagram before writing any SQL. What does an ER diagram
represent in relational database design?

```
An Entity Relationship (ER) Diagram visually represents:

Entities (Tables)
Attributes (Columns)
Relationships
Primary Keys
Foreign Keys

It helps design a normalized relational database before implementation.

```