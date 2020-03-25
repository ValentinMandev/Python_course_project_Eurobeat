import pandas as pd
import sqlite3
import re
from bs4 import BeautifulSoup
import urllib.request
import os
import random


def load_database():
    if os.path.exists('database.db'):
        os.remove('all_songs.db')
        os.rename(r'database.db', r'all_songs.db')

    connector = sqlite3.connect('all_songs.db')
    query = connector.execute('SELECT * from all_songs')

    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    return results



def show_info(search_field):
    results = load_database()
    s_songs = dict()
    c = 1
    for songs in range(len(results['song_name'])):
        s = re.compile(search_field, re.I)
        if s.search(results['song_name'][songs]) or s.search(results['artist_name'][songs]) or s.search(str(results['release_year'][songs])) \
                or s.search(results['label'][songs]) or s.search(results['artist_name'][songs] + ' ' + results['song_name'][songs]) \
                or s.search(results['artist_name'][songs] + ' - ' + results['song_name'][songs]):
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
    results = load_database()
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
        txt = str(text).replace('</a><br/>', '').replace('&amp;', '&').replace('<b>#:</b><p align="left">', '')\
            .replace('[<div class="mmids">\n', '').replace('</div>]', '').replace('<br/>', '')

        with open('updated_lyrics_file.txt', 'w') as outfile:
            end_title_index = txt.index('>Search database') + len('>Search database')
            print(txt[end_title_index:], file=outfile)


    for songs in range(len(results['song_id'])):
        if results['song_id'][songs] == song_id:
            sname = [None]
            sname[0] = (f"{results['artist_name'][songs]} - {results['song_name'][songs]}")
            if results['release_year'][songs] is not None and results['release_year'][songs] != 'None' and results['release_year'][songs] != '': sname.append(f"First release: {results['release_year'][songs]}")
            else: sname.append('First release: Unknown')
            if results['label'][songs] is not None and results['label'][songs] != 'None' and results['label'][songs] != '': sname.append(f"Music company: {results['label'][songs]}")
            else: sname.append('Music company: Unknown')
            if results['producer'][songs] is not None and results['producer'][songs] != 'None' and results['producer'][songs] != '': sname.append(f"Produced by: {results['producer'][songs]}")
            else: sname.append('Produced by: Unknown')
            if results['song_writer'][songs] is not None and results['song_writer'][songs] != 'None' and results['song_writer'][songs] != '': sname.append(f"Song writer: {results['song_writer'][songs]}")
            else: sname.append('Song writer: Unknown')
            sname.append(f"{results['youtube_search_link'][songs]}")
            if results['duration'][songs] is not None and results['duration'][songs] != 'None' and results['duration'][songs] != '': sname.append(f"Song duration: {results['duration'][songs]}")
            else: sname.append('Song duration: Unknown')
            if song_id < 100000: sname.append(f"Lyrics:\n{txt[end_title_index:]}")
            else: sname.append('Lyrics not available')
            return sname


def random_items():
    results = load_database()
    randoms = list()

    list_for_random_artist = []
    [list_for_random_artist.append(results['artist_name'][res]) for res in range(len(results))]
    list_for_random_artist = list(set(list_for_random_artist))
    randoms.append(random.choice(list_for_random_artist))

    list_for_random_year = []
    [list_for_random_year.append(results['release_year'][res]) for res in range(len(results)) if results['release_year'][res] != '' and results['release_year'][res] != None \
    and results['release_year'][res] != 'Year' and results['release_year'][res] != 'Unreleased' and results['release_year'][res] != 'Unreleased?']
    list_for_random_year = list(set(list_for_random_year))
    randoms.append(random.choice(list_for_random_year))

    list_for_random_label = []
    [list_for_random_label.append(results['label'][res]) for res in range(len(results)) if results['label'][res] != '' and results['label'][res] != None]
    list_for_random_label = list(set(list_for_random_label))
    randoms.append(random.choice(list_for_random_label))

    return randoms

