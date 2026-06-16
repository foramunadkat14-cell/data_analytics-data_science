1. Create two tables in your database: 'restaurants' (id, name, city) and 'dishes' (id, restaurant_id, dish_name, price). Insert at least 3 restaurants and 2-3 dishes for each restaurant.

**restaurants Table**
```
CREATE TABLE restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);
```
**dishes Table**

```
CREATE TABLE dishes (
    id INT PRIMARY KEY,
    restaurant_id INT,
    dish_name VARCHAR(100),
    price DECIMAL(10,2)
);
```

2. Write an SQL INNER JOIN query to display each dish along with its restaurant name and city, similar to how Zomato shows dish details with the restaurant info.

```
SELECT
    d.dish_name,
    d.price,
    r.name AS restaurant_name,
    r.city
FROM dishes d
INNER JOIN restaurants r
ON d.restaurant_id = r.id;
```

3. Write an SQL LEFT JOIN query to list all restaurants and their dishes, showing restaurants even if they currently have no dishes on the menu.<br><br><em><strong>Hint:</strong> Use LEFT JOIN so restaurants without dishes still appear in the results with NULL for dish columns.</em>

```
SELECT restaurants.name, restaurants.city, dishes.dish_name FROM restaurants LEFT JOIN dishes ON restaurants.rid = dishes.rid;
```

4. Write an SQL RIGHT JOIN query to display all dishes and their restaurant names, including any dishes that might not be linked to a restaurant (simulate a data error where a dish has a restaurant_id that doesn't match any restaurant).

```
SELECT dishes.dish_name,restaurants.name,restaurants.city FROM dishes RIGHT JOIN restaurants on dishes.rid=restaurants.rid
```

5. Given this scenario: You want to show a list of all playlists and the songs inside them, like Spotify. Explain which JOIN type (INNER, LEFT, or RIGHT) you would use to show all playlists, even if some are empty, and write the SQL query for it.

```
SELECT playlists.playlist_name,
   songs.song_name
```
