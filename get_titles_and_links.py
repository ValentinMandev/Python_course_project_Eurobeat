from bs4 import BeautifulSoup
import urllib.request

# Creating the list with artist name index and adding the first page:
all_lyrics_index = ['https://www.eurobeat-prime.com/lyrics.php?artist=1']


# Filling the list with the rest of the pages (letters from A to Z)
for letter in range(ord('a'), ord('z') + 1):
    all_lyrics_index.append(f'https://www.eurobeat-prime.com/lyrics.php?artist={chr(letter)}')


# Getting a file with all available songs plus links for lyrics:
lines_in_file = 1
with open('all_songs.txt', 'w') as outfile:
    for page in all_lyrics_index:
        html_page = urllib.request.urlopen(page)
        soup = BeautifulSoup(html_page)
        print(soup.findAll("div", class_="mmids"), file=outfile)
        lines_in_file += 1


# Обработка на файла - премахваме излишни неща, пълним отделни променливи за име на изпълнител, име на песен, линк и
# ID (което взимаме от ID-то от линка с текста на песента).
# Пълним списък от списъци с необходимата ни информация
artist_song_list = [[] for _ in range(10000)]
line_number = 0
with open('all_songs.txt') as outfile:
    for line in outfile:
        if line != '[<div class="mmids">\n' and line != '</div>]\n' and line != '</p>\n': # изключва излишни редове
            txt = str(line).replace('</a><br/>', '').replace('<br/>', '').replace('&amp;', '&').replace('<b>#:</b><p align="left">', '') # премахва ненужните html елементи
            if '<b>' not in txt:
                song_id = txt[txt.index('?lyrics=') + 8:txt.index('">')]
                artist_name = txt[:txt.index(' - <a href="?lyrics=')]
                song_name = txt[len(txt) - txt[::-1].index('>'):].replace('\n', '')
                lyrics_link = 'https://www.eurobeat-prime.com/lyrics.php?lyrics=' + song_id
                artist_song_list[line_number] = list()
                artist_song_list[line_number].append(song_id)
                artist_song_list[line_number].append(artist_name)
                artist_song_list[line_number].append(song_name)
                artist_song_list[line_number].append(lyrics_link)
                line_number += 1

print(artist_song_list)

