import pandas as pd
import sqlite3
import re

connector = sqlite3.connect('all_songs.db')
query = connector.execute('SELECT * from all_songs')

cols = [column[0] for column in query.description]
results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

search_field = input('Search for a song, artist, year or label ')

for songs in range(len(results['song_name'])):
    s = re.compile(search_field, re.I)
    if s.search(results['song_name'][songs]) or s.search(results['artist_name'][songs]) or s.search(str(results['release_year'][songs])) or s.search(results['label'][songs]):
        print(results['artist_name'][songs], '-', results['song_name'][songs], f"{'(' + str(results['release_year'][songs]) + ')' if results['release_year'][songs] is not None else ''}")

