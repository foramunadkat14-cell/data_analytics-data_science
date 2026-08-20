#1. Create a Python script that imports the math module and uses math.sqrt() to calculate and print the square root of 225.

import math
number = 225
result = math.sqrt(number)
print(f"The square root of {number} is {result}")

#2. Write a script that uses the os module to create a new folder named 'MyDownloads' in your current working directory, then print the absolute path of the new folder.

import os
folder_name = 'MyDownloads'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")
absolute_path = os.path.abspath(folder_name)
print(f"Absolute path: {absolute_path}")

#3. Use the datetime module to get the current date and time, then format and print it as 'DD-MM-YYYY HH:MM:SS', similar to how WhatsApp shows message timestamps.<br><br><em><strong>Hint:</strong> Use strftime() to format the output.</em>

from datetime import datetime
current_time = datetime.now()
formatted_timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")
print(f"Timestamp: {formatted_timestamp}")

#4. Create a custom Python module called playlist_utils.py with a function add_song(playlist, song) that adds a song to a list. Import this module in another script and use it to add three songs to a playlist, then print the final playlist.

from datetime import datetime
current_time = datetime.now()
formatted_timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")
print(f"Timestamp: {formatted_timestamp}")

#5. Set up a new virtual environment using venv, activate it, and install the 'requests' package using pip. Write a short script that imports requests and prints the version installed.<br><br><em><strong>Hint:</strong> Use 'python -m venv venv_folder', then 'pip install requests'.</em>

def add_song(playlist, song):
    playlist.append(song)
    print(f"Added '{song}' to the playlist.")
    return playlist