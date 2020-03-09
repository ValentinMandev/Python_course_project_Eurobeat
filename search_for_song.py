import pandas as pd
import sqlite3
import re
from bs4 import BeautifulSoup
import urllib.request


connector = sqlite3.connect('all_songs.db')
query = connector.execute('SELECT * from all_songs')

cols = [column[0] for column in query.description]
results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

# search_field = input('Search for a song, artist, year or label ')
#
# for songs in range(len(results['song_name'])):
#     s = re.compile(search_field, re.I)
#     if s.search(results['song_name'][songs]) or s.search(results['artist_name'][songs]) or s.search(str(results['release_year'][songs])) or s.search(results['label'][songs]):
#         print(results['artist_name'][songs], '-', results['song_name'][songs], f"{'(' + str(results['release_year'][songs]) + ')' if results['release_year'][songs] is not None and results['release_year'][songs] is not '' else ''}")


song_id = 4069
# Минаваме през всички страници и записваме файл с имена и линкове за всички песни:
with open('temporary_lyrics_file.txt', 'w') as tempfile:
    lyrics_page = urllib.request.urlopen(f'https://www.eurobeat-prime.com/lyrics.php?lyrics={song_id}')
    soup = BeautifulSoup(lyrics_page, 'html.parser')
    text = soup.findAll("div", class_="mmids")
txt = str(text).replace('</a><br/>', '').replace('&amp;', '&').replace('<b>#:</b><p align="left">', '').replace('[<div class="mmids">\n', '').replace('</div>]', '').replace('<br/>', '')


with open('updated_lyrics_file.txt', 'w') as outfile:
    end_title_index = txt.index('>Search database') + len('>Search database')
    print(txt[end_title_index:], file=outfile)


