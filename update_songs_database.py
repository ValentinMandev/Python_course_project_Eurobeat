import sqlite3
from get_titles_and_links import artist_song_list
import os

os.remove("all_songs.db")

data = list()
for lst in range(len(artist_song_list)):
	if len(artist_song_list[lst]) > 0:
		data.append(tuple(artist_song_list[lst]))

connector = sqlite3.connect("all_songs.db")
cursor = connector.cursor()


cursor.execute('''CREATE TABLE all_songs
             (song_id NUMERIC NOT NULL, artist_name text, song_name text, lyrics_link text)''')

cursor.executemany("INSERT INTO all_songs VALUES (?,?,?,?)", data)

connector.commit()

cursor.close()
connector.close()


