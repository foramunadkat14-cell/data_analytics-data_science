1. Create a table called Restaurants with columns: id, name, cuisine, rating, and city. Insert at least 5 sample records representing real or fictional restaurants you might find on Zomato.

```
CREATE TABLE Restaurants ( rid int PRIMARY KEY AUTO_INCREMENT, name varchar(255), cuisine varchar(255), rating ENUM ('1 star','2 star','3 star','4 star','5 star'), city varchar(255) )
```

2. Write a SQL query to find all restaurants in the Restaurants table that have a rating greater than 4.0 and are located in either 'Ahmedabad' or 'Surat'.

```
SELECT * FROM Restaurants WHERE rating > 4 AND city LIKE 'A%';
```

3. Using the LIKE operator, write a query to select all restaurants whose names start with 'Swa' (for example, 'Swagat', 'Swadisht') from the Restaurants table.<br><br><em><strong>Hint:</strong> Use LIKE 'Swa%'.</em>

```
SELECT * FROM restaurants WHERE name LIKE 'sWA%'
```

4. Write a SQL query using the BETWEEN keyword to find all restaurants in the Restaurants table with a rating between 3.5 and 4.5 (inclusive).

```
SELECT * FROM restaurants WHERE rating BETWEEN 3 AND 4
```

5. Write a query to find all restaurants whose cuisine is either 'Chinese', 'Italian', or 'South Indian' using the IN operator.

```
SELECT * FROM restaurants WHERE cuisine in ('Chinese','Italian','South Indian')
```
