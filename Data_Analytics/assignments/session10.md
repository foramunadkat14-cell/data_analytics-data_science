1. Create two tables: Influencers (id, name) and Collaborations (id, influencer1_id, influencer2_id, collab_date). Write a SQL FULL JOIN query to list all influencers and show their collaboration partner names if any, including influencers with no collaborations.

```
SELECT collaborations.collab_date,influencers.name FROM collaborations JOIN influencers on collaborations.ifid=influencers.ifid
```

2. Using a SELF JOIN, write a query on a table called Playlists (id, user_id, playlist_name, parent_playlist_id) to display each playlist alongside its parent playlist name, similar to how Spotify shows nested playlists.<br><br><em><strong>Hint:</strong> Join Playlists with itself on parent_playlist_id = id.</em>

```
SELECT child.playlist_name, parent.playlist_name AS parent_playlist FROM Playlists child LEFT JOIN Playlists parent ON child.parent_playlist_id = parent.id;
```

3. Given three tables: Users (id, username), Orders (id, user_id, order_date), and Payments (id, order_id, amount), write a SQL query using multiple JOINs to display each username, their order date, and payment amount, showing all users even if they have no orders or payments.

```
SELECT users.username,
   orders.order_date,
   payments.amount
FROM users LEFT JOIN orders ON users.id = orders.user_id LEFT JOIN payments ON orders.id = payments.order_id;
```

4. You notice that your JOIN query between Zomato's Restaurants and Reviews tables is returning duplicate rows for some restaurants. Modify your query to eliminate duplicates and explain in one line why the duplicates were happening.<br><br><em><strong>Hint:</strong> Use DISTINCT or GROUP BY and consider the relationship between restaurants and reviews.</em>

```
SELECT DISTINCT restaurants.name, reviews.review_text FROM restaurants JOIN reviews ON restaurants.id = reviews.restaurant_id;
```
Duplicates were happening because one restaurant can have multiple reviews, so the JOIN returned one row for each matching review

5. Write two different JOIN queries on a Products and Categories table (like Flipkart) to list all products with their category names, but use different join conditions in each. Briefly explain which join condition is more efficient and why.

**QURY 1**

```
SELECT products.product_name, categories.category_name FROM products JOIN categories ON products.category_id = categories.category_id;
```

**QUERY 2**

```
SELECT p.product_name, c.category_name FROM products p JOIN categories c ON p.category_id = c.category_id;
```
Both queries perform the same and are equally efficient because they use the same join condition:
