#1. Create a text file named playlist.txt and write the names of 5 songs you listened to this week, each on a new line using Python's open() function in write mode.

songs = ["Blinding Lights", "Levitating", "Shape of You", "Senorita", "Starboy"]
with open("playlist.txt", "w") as file:
    for song in songs:
        file.write(song + "\n")


#2. Read the playlist.txt file you created and display each song name in uppercase letters using Python.

with open("playlist.txt", "r") as file:
    for line in file:
        print(line.strip().upper())


#3. Download a sample CSV file of IPL match scores (you can create your own with columns: match_id, team1, team2, winner) and write a Python script to read the file and print the winner of each match using the csv module.


import csv
csv_data = [
    ["match_id", "team1", "team2", "winner"],
    ["1", "Mumbai Indians", "Chennai Super Kings", "Chennai Super Kings"],
    ["2", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Royal Challengers Bangalore"],
    ["3", "Gujarat Titans", "Rajasthan Royals", "Gujarat Titans"]
]

with open("ipl_scores.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
with open("ipl_scores.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Match {row['match_id']} Winner: {row['winner']}")


#4. Find a public JSON file of trending movies (or create your own movies.json with at least 3 movie objects containing title, year, and rating), then use the json module in Python to load the file and print the title and rating of each movie.


import json

movies_data = [
    {"title": "Dune: Part Two", "year": 2024, "rating": 8.8},
    {"title": "Oppenheimer", "year": 2023, "rating": 8.3},
    {"title": "Interstellar", "year": 2014, "rating": 8.7}
]

with open("movies.json", "w") as file:
    json.dump(movies_data, file, indent=4)
with open("movies.json", "r") as file:
    movies = json.load(file)
    for movie in movies:
        print(f"Title: {movie['title']} | Rating: {movie['rating']}")



#5. Use the pathlib module to check if a file called 'my_fav_apps.json' exists in your current directory, and if not, create it and write a JSON array of your top 3 mobile apps (e.g., Instagram, Zomato, Paytm) with their names and categories.<br><br><em><strong>Hint:</strong> Use Path('my_fav_apps.json').exists() to check for the file, and json.dump() to write the data.</em>

import json
from pathlib import Path
file_path = Path('my_fav_apps.json')
if not file_path.exists():
    fav_apps = [
        {"name": "Study solution AI", "category": "Education"},
        {"name": "Zomato", "category": "Food Delivery"},
        {"name": "Groww", "category": "Finance"}
    ]
    with open(file_path, "w") as file:
        json.dump(fav_apps, file, indent=4)
        
    print("File 'my_fav_apps.json' created and data written successfully.")
else:
    print("The file 'my_fav_apps.json' already exists.")