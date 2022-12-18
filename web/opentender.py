import requests
from bs4 import BeautifulSoup
import csv


req = requests.get("https://opentender.eu/start")
soup = BeautifulSoup(req.content, "html.parser")

#print(soup) 
#print(soup.text) 

gun = soup.find('ul',class_='portal-links')
#print(gun.text) 
#print(gun)
titles_list = []
 
count = 1
for title in gun:
    d = {}
    d['Title Number'] = f'li {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)
 
filename = 'opentender.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()
     
    w.writerows(titles_list)
