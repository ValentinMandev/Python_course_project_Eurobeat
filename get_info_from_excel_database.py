import urllib.request

url = 'https://drive.google.com/u/0/uc?id=1HAuDZ-jPWco90VF1A9yfBwlXgxdP5Obu&export=download'
excel_database = 'full_database.xlsx'

urllib.request.urlretrieve(url, excel_database)
