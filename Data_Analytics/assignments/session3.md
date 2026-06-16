1. Create a table called Playlist with columns: id (INT, primary key), song_name (VARCHAR), artist (VARCHAR), and duration (INT, seconds). Insert a single row for your current favorite song.

**table**

```
CREATE TABLE Playlist (
 pid int PRIMARY KEY AUTO_INCREMENT,
 song_name varchar(255),
 artist varchar(255),
 duration int 
 )
```
![alt text](image.png)


2. Insert 3 new rows into the Playlist table for songs you recently listened to on Spotify, including their song_name, artist, and duration.

```
INSERT INTO Playlist (id, song_name, artist, duration)
VALUES
(2, 'Kesariya', 'Arjit Singh', 269),
(3, 'Brown Munde', 'AP Dhillon', 250),
(4, 'Levitating', 'Dua Lipa', 203);
```


3. Update the artist name for one of your Playlist entries to fix a typo (for example, change 'Arjit Singh' to 'Arijit Singh') using the UPDATE statement with a WHERE clause.

```
UPDATE Playlist SET artist = 'Arijit Singh' WHERE artist = 'Arjit Singh';
```

4. Delete a song from the Playlist table where the duration is less than 120 seconds using the DELETE statement and a WHERE clause.<br><br><em><strong>Hint:</strong> Make sure your WHERE clause is specific so you don’t accidentally delete all rows.</em>

```
DELETE FROM Playlist WHERE duration < 120;
```

5. Write an SQL statement that would update the song_name for all songs by 'AP Dhillon' in your Playlist to add '(Remix)' at the end of the name, but only if the duration is more than 180 seconds.<br><br><em><strong>Constraint:</strong> Combine UPDATE with WHERE to target only the correct rows.</em>

```
UPDATE Playlist SET song_name = CONCAT(song_name, ' (Remix)') WHERE artist = 'AP Dhillon'  AND duration > 180;
```