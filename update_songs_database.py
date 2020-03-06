import sqlite3
from get_titles_and_links import artist_song_list
import os

# Изчиствам си базата данни, когато я свалям наново
os.remove("all_songs.db")


connector = sqlite3.connect("all_songs.db")
cursor = connector.cursor()


cursor.execute('''CREATE TABLE all_songs (song_id NUMERIC NOT NULL, artist_name text, song_name text, lyrics_link text)''')

cursor.executemany("INSERT INTO all_songs VALUES (?,?,?,?)", artist_song_list)

connector.commit()

cursor.close()
connector.close()


