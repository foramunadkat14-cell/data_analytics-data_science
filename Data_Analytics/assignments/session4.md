1. Create a table named MusicPlaylist with columns: id, song_name, artist, genre, and duration. Insert at least 5 records representing songs from your favorite Spotify playlist, then write a SELECT statement to retrieve all columns for all songs.

**table**
```
CREATE TABLE MusicPlaylist ( mid int PRIMARY KEY AUTO_INCREMENT, song_name varchar(255), artist varchar(255), genre varchar(255), duration time )
```

**SELECT statement to retrieve all columns for all songs**
```
SELECT * FROM music_playlist
```

2. Write a SQL query to display only the song_name and artist columns from the MusicPlaylist table, showing just the first 3 records using the LIMIT keyword.

```
SELECT song_name,artist FROM music_playlist LIMIT 0,3;
```

3. Suppose you have a table named FoodOrders with columns: id, restaurant, food_item, and order_date. Write a SQL query to list all unique restaurant names where you have placed orders, using the DISTINCT keyword.

```
SELECT DISTINCT ('restaurant') FROM FoodOrders
```

4. Write a SQL query on the FoodOrders table to select food_item as 'Dish' and order_date as 'Date Ordered', displaying only these two columns with the column aliases in the output.

```
SELECT food_item AS 'dish', order_date as 'Date Ordered' from FoodOrders
```

5. You tried running this query: SELECT DISTINCT food_item, restaurant FROM FoodOrders LIMIT 2, but it returns an error or doesn't work as expected. Identify and fix the mistake in the query.<br><br><em><strong>Hint:</strong> Check the correct placement and usage of the LIMIT keyword in SQL syntax.</em>

you need to have 2 numbers in the limit to run this query propely