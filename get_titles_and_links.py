from bs4 import BeautifulSoup
import urllib.request
import os


# Създаваме списък, който ще държи всички страници (за всяка една буква, с която започва името на изпълнителя):
# Първият елемент е за тези, чийто псевдоним започва с число
all_lyrics_index = ['https://www.eurobeat-prime.com/lyrics.php?artist=1']


# Допълваме листа с буквите от A до Z
for letter in range(ord('a'), ord('z') + 1):
    all_lyrics_index.append(f'https://www.eurobeat-prime.com/lyrics.php?artist={chr(letter)}')


# Минаваме през всички страници и записваме файл с имена и линкове за всички песни:
with open('all_songs.txt', 'w') as outfile:
    for page in all_lyrics_index:
        html_page = urllib.request.urlopen(page)
        soup = BeautifulSoup(html_page, 'html.parser')
        print(soup.findAll("div", class_="mmids"), file=outfile)


# Обработка на информацията от файла - премахваме излишни неща, пълним отделни променливи за име на изпълнител, име на песен, линк и
# ID (което взимаме от ID-то от линка с текста на песента).
# Пълним списък от списъци с необходимата ни информация
artist_song_list_raw = [[] for _ in range(10000)] # тук дефинирам някаква голяма бройка списъци съдържащи се в основния списък, за да съм сигурен, че няма да ми даде out of range. Списъка на песни е повече от два пъти по-малко.
line_number = 0
with open('all_songs.txt') as input_file:
    for line in input_file:
        if line != '[<div class="mmids">\n' and line != '</div>]\n' and line != '</p>\n': # изключва излишни редове
            txt = str(line).replace('</a><br/>', '').replace('<br/>', '').replace('&amp;', '&').replace('<b>#:</b><p align="left">', '') # премахва ненужните html елементи
            if '<b>' not in txt:
                song_id = txt[txt.index('?lyrics=') + 8:txt.index('">')]
                artist_name = txt[:txt.index(' - <a href="?lyrics=')]
                song_name = txt[len(txt) - txt[::-1].index('>'):].replace('\n', '')
                lyrics_link = 'https://www.eurobeat-prime.com/lyrics.php?lyrics=' + song_id
                artist_song_list_raw[line_number].append(str(artist_name) + ' - ' + str(song_name))
                artist_song_list_raw[line_number].append(song_id)
                artist_song_list_raw[line_number].append(artist_name)
                artist_song_list_raw[line_number].append(song_name)
                artist_song_list_raw[line_number].append(lyrics_link)
                artist_song_list_raw[line_number].append('https://www.youtube.com/results?search_query=' + artist_name.replace(' ', '+').replace('&', 'and') + '+-+' + song_name.replace(' ', '+').replace('&', 'and'))
                line_number += 1


# Изчиствам си празните списъци от списъка с данни
artist_song_list = list()
for lst in range(len(artist_song_list_raw)):
    if len(artist_song_list_raw[lst]) > 0:
        artist_song_list.append(artist_song_list_raw[lst])


# Изтривам ненужния all_songs.txt
os.remove("all_songs.txt")

