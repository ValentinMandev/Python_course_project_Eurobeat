# from bs4 import BeautifulSoup
# import urllib.request
#
#
# # Creating the list with artist name index and adding the first page:
# all_lyrics_index = ['https://www.eurobeat-prime.com/lyrics.php?artist=1']
#
#
# # Filling the list with the rest of the pages (letters from A to Z)
# for letter in range(ord('a'), ord('z') + 1):
#     all_lyrics_index.append(f'https://www.eurobeat-prime.com/lyrics.php?artist={chr(letter)}')
#
#
# # Getting a file with all available songs plus links for lyrics:
# with open('all_songs.txt', 'w') as outfile:
#     for page in all_lyrics_index:
#         html_page = urllib.request.urlopen(page)
#         soup = BeautifulSoup(html_page)
#         print(soup.findAll("div", class_="mmids"), file=outfile)


# Editing outfile:
with open('all_songs.txt') as outfile:
	for line in outfile:
		if line != '[<div class="mmids">\n' and line != '</div>]\n' and line != '</p>\n':
			print(line)



