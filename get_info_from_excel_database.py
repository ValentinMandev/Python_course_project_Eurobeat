import urllib.request
import openpyxl

url = 'https://drive.google.com/u/0/uc?id=1ImiITsoRt5CwaEUEgYJ__QUFZbaZ2pct&export=download'
excel_database = 'full_database.xlsx'

urllib.request.urlretrieve(url, excel_database)

workbook = openpyxl.load_workbook(filename=excel_database)
sheets = workbook.sheetnames

for sheet in sheets:
    print(workbook[sheet]['A2'].value)

