import urllib.request
import openpyxl

url = 'https://drive.google.com/u/0/uc?id=18mC9wWEt3sTxomev4EUiVOvTUrJgGMJ0&export=download'
excel_database = 'full_database.xlsx'

urllib.request.urlretrieve(url, excel_database)

workbook = openpyxl.load_workbook(filename=excel_database)
sheets = workbook.sheetnames


information_from_excel_file_raw = [[] for _ in range(60000)]
a = 0

for sheet in sheets:
    for n in range(2, 2000):
        if workbook[sheet][f'B{n}'].value and workbook[sheet][f'C{n}'].value and workbook[sheet][f'B{n}'].value:
            release_year = workbook[sheet][f'A{n}'].value
            artist_name = workbook[sheet][f'B{n}'].value
            song_name = workbook[sheet][f'C{n}'].value
            duration = str(workbook[sheet][f'D{n}'].value)
            song_writer = workbook[sheet][f'E{n}'].value
            producer = workbook[sheet][f'F{n}'].value
            label = workbook[sheet][f'G{n}'].value
            information_from_excel_file_raw[a].append(str(artist_name) + ' - ' + str(song_name))
            information_from_excel_file_raw[a].append(str(artist_name))
            information_from_excel_file_raw[a].append(str(song_name))
            information_from_excel_file_raw[a].append(release_year)
            information_from_excel_file_raw[a].append(duration)
            information_from_excel_file_raw[a].append(song_writer)
            information_from_excel_file_raw[a].append(producer)
            information_from_excel_file_raw[a].append(label)
            a += 1

# Изчиствам си празните списъци от списъка с данни
information_from_excel_file = list()
for lst in range(len(information_from_excel_file_raw)):
    if len(information_from_excel_file_raw[lst]) > 0:
        information_from_excel_file.append(information_from_excel_file_raw[lst])




