import sqlite3
from get_titles_and_links import artist_song_list
from get_info_from_excel_database import information_from_excel_file
import os

# Merge-вам двата вида данни в едно:
s = list()
for l in range(len(artist_song_list)):
    for m in range(len(information_from_excel_file)):
        if str(artist_song_list[l][0]).lower() == str(information_from_excel_file[m][0]).lower():
            artist_song_list[l].append(information_from_excel_file[m][3])
            artist_song_list[l].append(information_from_excel_file[m][4])
            artist_song_list[l].append(information_from_excel_file[m][5])
            artist_song_list[l].append(information_from_excel_file[m][6])
            artist_song_list[l].append(information_from_excel_file[m][7])
            s.append(m) # тук добавяме всички елементи от information_from_excel_file, за които сме намерили съответствие с artist_song_list, за да ги разкараме после, понеже вече не ни трябват
s = sorted(s, reverse=True)

for items in s:
    del information_from_excel_file[items] # трием повтарящите се елементи


# Добавяме празни елементи за песните, които се срещат в artist_song_list, но не и в information_from_excel_file
for songs in range(len(artist_song_list)):
    if len(artist_song_list[songs]) == 6:
        artist_song_list[songs].append('')
        artist_song_list[songs].append('')
        artist_song_list[songs].append('')
        artist_song_list[songs].append('')
        artist_song_list[songs].append('')


# Обработваме елементите от information_from_excel_file, които липсват в artist_song_list
id_excel = 100000
for songs in range(len(information_from_excel_file)):
    if len(information_from_excel_file[songs]) == 8:
        information_from_excel_file[songs].insert(3, '')
        information_from_excel_file[songs].insert(3, '')
        information_from_excel_file[songs].insert(1, f'{id_excel}')
        information_from_excel_file[songs][5] = 'https://www.youtube.com/results?search_query=' + str(information_from_excel_file[songs][2]).replace('&', 'and') + ' - ' + str(information_from_excel_file[songs][3]).replace('&', 'and')
        id_excel += 1

# Добавяме останалите елементи в information_from_excel_file към artist_song_list
artist_song_list += information_from_excel_file

# Махаме елементите във формат 'Artist name - Song name', които бяхме създали, за да идентифицираме общите песни между двата вида данни
for songs in range(len(artist_song_list)):
    del artist_song_list[songs][0]

database = 'database.db'



# Изчиствам си старата база данни
if os.path.exists(database):
    os.remove(database)



# Създавам си новата база данни, в която включвам цялата нужна информация:
connector = sqlite3.connect(database)
cursor = connector.cursor()

cursor.execute('''CREATE TABLE all_songs (song_id NUMERIC NOT NULL, artist_name text, song_name text, lyrics_link text, youtube_search_link text, release_year numeric, duration text, song_writer text, producer text, label text)''')

cursor.executemany("INSERT INTO all_songs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", artist_song_list)

connector.commit()

cursor.close()
connector.close()




