import pandas as pd
import sqlite3
import re
from bs4 import BeautifulSoup
import urllib.request


connector = sqlite3.connect('all_songs.db')
query = connector.execute('SELECT * from all_songs')

cols = [column[0] for column in query.description]
results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)


def show_info(search_field):
    s_songs = dict()
    c = 1
    for songs in range(len(results['song_name'])):
        s = re.compile(search_field, re.I)
        if s.search(results['song_name'][songs]) or s.search(results['artist_name'][songs]) or s.search(str(results['release_year'][songs])) or s.search(results['label'][songs]) or s.search(results['artist_name'][songs] + ' ' + results['song_name'][songs]) or s.search(results['artist_name'][songs] + ' - ' + results['song_name'][songs]):
            s_songs[c] = (results['artist_name'][songs] + ' - ' + results['song_name'][songs], results['song_id'][songs])
            c += 1

    found_songs = []
    any_songs = False
    for found in s_songs:
        any_songs = True
        found_songs.append(f'{s_songs[found][0]}')
    if any_songs is False:
        found_songs = ['Sorry, no songs matching your query!', 'Try again!']
    return found_songs


def print_song_info():
    with open('chosen_song.txt') as songfile:
        song_name = str([song for song in songfile]).replace("['", '').replace("\\n']", '').replace('["', '').replace('\\n"]', '')

    song_id = int()

    for songs in range(len(results['song_id'])):
        if song_name == results['artist_name'][songs] + ' - ' + results['song_name'][songs]:
            song_id = results['song_id'][songs]

    if 0 < song_id:
        with open('temporary_lyrics_file.txt', 'w') as tempfile:
            lyrics_page = urllib.request.urlopen(f'https://www.eurobeat-prime.com/lyrics.php?lyrics={song_id}')
            soup = BeautifulSoup(lyrics_page, 'html.parser')
            text = soup.findAll("div", class_="mmids")
        txt = str(text).replace('</a><br/>', '').replace('&amp;', '&').replace('<b>#:</b><p align="left">', '').replace('[<div class="mmids">\n', '').replace('</div>]', '').replace('<br/>', '')

        with open('updated_lyrics_file.txt', 'w') as outfile:
            end_title_index = txt.index('>Search database') + len('>Search database')
            print(txt[end_title_index:], file=outfile)


    for songs in range(len(results['song_id'])):
        if results['song_id'][songs] == song_id:
            sname = [None]
            sname[0] = (f"{results['artist_name'][songs]} - {results['song_name'][songs]}")
            if results['release_year'][songs] is not '': sname.append(f"First release: {results['release_year'][songs]}")
            else: sname.append('First release: Unknown')
            if results['label'][songs] is not None: sname.append(f"Music company: {results['label'][songs]}")
            else: sname.append('Music company: Unknown')
            if results['producer'][songs] is not '': sname.append(f"Produced by: {results['producer'][songs]}")
            else: sname.append('Produced by: Unknown')
            if results['song_writer'][songs] is not '': sname.append(f"Song writer: {results['song_writer'][songs]}")
            else: sname.append('Song writer: Unknown')
            sname.append(f"YouTube search link: {results['youtube_search_link'][songs]}")
            if results['duration'][songs] is not '': sname.append(f"Song duration: {results['duration'][songs]}")
            else: sname.append('Song duration: Unknown')
            if song_id < 100000: sname.append(f"Lyrics:\n{txt[end_title_index:]}")
            else: sname.append('Lyrics not available')
            return sname
