1. Create a table called Orders with columns: order_id, user_name, total_amount, and order_date. Insert 5 sample rows with different users and order amounts, including at least one NULL value for total_amount.

```
CREATE TABLE orders ( order_id int PRIMARY KEY AUTO_INCREMENT, user_name varchar(255), total_amount int, orderd_date date )
```

2. Write a SQL query to count how many orders were placed by each user in the Orders table, displaying user_name and the number of orders as order_count.

```
SELECT user_name, COUNT(*) AS order_count FROM Orders GROUP BY user_name
```

3. Write a SQL query to calculate the average total_amount of all orders in the Orders table, making sure to ignore any NULL values.

```
SELECT AVG(total_amount)FROM Orders
```

4. Suppose you are building a Flipkart-style dashboard: Write a SQL query to find the highest and lowest order amounts (MAX and MIN) from the Orders table, and display both values in a single result row.

```
SELECT MAX(total_amount) as max_amount,MIN(total_amount) as min_amount FROM orders
```
5. Write a SQL query to calculate the total sales (SUM of total_amount) for all orders, but only include orders where total_amount is not NULL.<br><br><em><strong>Hint:</strong> Use a WHERE clause to filter out NULL values before applying the SUM function.</em>

```
SELECT SUM(total_amount) FROM orders WHERE total_amount is not null
```
