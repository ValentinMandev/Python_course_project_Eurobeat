from bs4 import BeautifulSoup
import urllib.request
import re
import requests


# Creating the list with artist name index and adding the first page:
all_lyrics_index = ['https://www.eurobeat-prime.com/lyrics.php?artist=1']


# # Filling the list with the rest of the pages (letters from A to Z)
# for letter in range(ord('a'), ord('z') + 1):
#     all_lyrics_index.append(f'https://www.eurobeat-prime.com/lyrics.php?artist={chr(letter)}')


# # Getting all song lyrics links from all artist pages
# for page in all_lyrics_index:
#     html_page = urllib.request.urlopen(page)
#     soup = BeautifulSoup(html_page)
#     for link in soup.findAll('a', attrs={'href': re.compile("lyrics=")}):
#         print('https://www.eurobeat-prime.com/lyrics.php' + link.get('href'))


prices = urllib.request.urlopen('https://www.eurobeat-prime.com/lyrics.php?artist=d')
soup = BeautifulSoup(prices)
price = soup.findAll("div", class_="mmids")
print(prices)

# for price in prices:
#     price_parent = price.parent
#     price = int(''.join(price.text.split()[:2]))
#     print(f'Цена: {price}')

