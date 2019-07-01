import sqlite3
from bs4 import BeautifulSoup
import requests
DB = sqlite3.connect('Seasons.db')
CURSOR = DB.cursor()
CURSOR.execute('''CREATE TABLE IF NOT EXISTS season(NORTHERN HEMISPHERE TEXT, SOUTHERN HEMISPHERE TEXT, START DATE TEXT,END DATE TEXT);''')
LIST1 = []
WIKI = "https://en.wikipedia.org/wiki/Season"
WEBSITE_URL = requests.get(WIKI).text
SOUP = BeautifulSoup(WEBSITE_URL, 'lxml')
MY_TABLE = SOUP.find('table', {'class':'wikitable'})
SEASON = MY_TABLE.find_all('td')
for i in SEASON:
    LIST1.append(i.text)
for i in range(0, len(LIST1), 4):
    CURSOR.execute('''INSERT INTO season VALUES(?,?,?,?);''', (LIST1[i+0], LIST1[i+1], LIST1[i+2], LIST1[i+3]))
DB.commit()
DB.close()
