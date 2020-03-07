import sqlite3
from get_titles_and_links import artist_song_list
import os

database = 'all_songs.db'

# Изчиствам си базата д.анни, когато я свалям наново
if os.path.exists(database):
    os.remove(database)


connector = sqlite3.connect(database)
cursor = connector.cursor()

cursor.execute('''CREATE TABLE all_songs (song_id NUMERIC NOT NULL, artist_name text, song_name text, lyrics_link text, youtube_search_link text)''')

cursor.executemany("INSERT INTO all_songs VALUES (?,?,?,?,?)", artist_song_list)

connector.commit()

cursor.close()
connector.close()


