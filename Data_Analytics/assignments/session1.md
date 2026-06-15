1. Install MySQL or PostgreSQL on your system and create a new database named 'music_streaming_app' using the command line or GUI tool of your choice.

```
CREATE DATABASE music_streaming_app;
```

2. Inside the 'music_streaming_app' database, create a table called 'playlists' with columns: playlist_id (integer, primary key), name (varchar), and created_by (varchar).

```
CREATE TABLE playlists( playlist_id int PRIMARY KEY AUTO_INCREMENT, name varchar(255), created_by varchar(255) )
```

3. Insert three sample rows into the 'playlists' table representing playlists like 'Bollywood Hits', 'Chill Vibes', and 'Workout Mix', each created by a different user.

```
INSERT INTO playlists (playlist_id, name, created_by)
VALUES
(1, 'Bollywood Hits', 'Amit'),
(2, 'Chill Vibes', 'Priya'),
(3, 'Workout Mix', 'Rahul');
```

4. Write an SQL SELECT query to display all playlists created by the user 'Amit' from the 'playlists' table.<br><br><em><strong>Hint:</strong> Use the WHERE clause to filter by the 'created_by' column.</em>

```
SELECT * FROM playlists WHERE created_by = 'Amit';
```

5. Open ChatGPT or Copilot and ask it to explain the difference between a table, a row, and a column in SQL using an example from a food delivery app like Zomato. Paste the explanation you receive into your assignment.

```
Table:
A table is a collection of related data organized into rows and columns. For example, in a food delivery app like Zomato, a table named Restaurants stores information about restaurants.

Column:
A column represents a specific attribute of the data. In the Restaurants table, columns might be:

restaurant_id
restaurant_name
city
rating

Each column stores one type of information.

Row:
A row represents a single record in the table. For example:

restaurant_id	restaurant_name	city	rating
101	Pizza Hub	Ahmedabad	4.5

This entire entry is one row because it contains all the details of a single restaurant.
```