# The internet is full data and information and it is possible to scrap data from websites using Python
# Let's scrap USA Presidents name from wikipedia using this link (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States)

# importing important packages
import requests
from bs4 import BeautifulSoup
from print import print

# US presidents list url

url ='https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)
content = response.content


soup = BeautifulSoup(content, 'html.parser')
title = soup.title.get_text()
print(title)

table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')[1:]

presidents = []
for row in rows:
    cells = row.find_all('td')
    for i, cell in enumerate(cells):
        if cell.find('b'):
           president = cell.find('b').find('a').text
           presidents.append(president)
           
print("presidents")



