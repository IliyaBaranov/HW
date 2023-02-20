import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
weather = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
full_page = requests.get(weather, headers=headers)
soup = BS(full_page.content, 'html.parser')

rate = soup.find_all('td')
rate2 = soup.find_all('th')

list1 = []
for p1 in rate:
    plist1 = list(p1)
    list1.append(plist1)
y1 = list(zip(*[iter(list1)]*12))

list2 = []
for p2 in rate2:
    plist2 = list(p2)
    list2.append(plist2)
y2 = list(zip(*[iter(list2)]*12))
inp = input('Please enter a city: ')
if inp == 'Heltermaa':
    print(y2[0], '\n', y1[0])
elif inp == 'Jõgeva':
    print(y2, '\n', y1[1])
elif inp == 'Jõhvi':
    print(y2, '\n', y1[2])
elif inp == 'Kihnu':
    print(y2, '\n', y1[3])
elif inp == 'Kunda':
    print(y2, '\n', y1[4])
elif inp == 'Kuressaare linn':
    print(y2, '\n', y1[5])
elif inp == 'Kuusiku':
    print(y2, '\n', y1[6])
elif inp == 'Lääne-Nigula':
    print(y2, '\n', y1[7])
elif inp == 'Narva':
    print(y2, '\n', y1[8])
elif inp == 'Pakri':
    print(y2, '\n', y1[9])
elif inp == 'Pärnu':
    print(y2, '\n', y1[10])
elif inp == 'Ristna':
    print(y2, '\n', y1[11])
elif inp == 'Roomassaare':
    print(y2, '\n', y1[12])
elif inp == 'Ruhnu':
    print(y2, '\n', y1[13])
elif inp == 'Sõrve':
    print(y2, '\n', y1[14])
elif inp == 'Tallinn-Harku':
    print(y2, '\n', y1[15])
elif inp == 'Tartu-Tõravere':
    print(y2, '\n', y1[16])
elif inp == 'Tiirikoja':
    print(y2, '\n', y1[17])
elif inp == 'Tooma':
    print(y2, '\n', y1[18])
elif inp == 'Türi':
    print(y2, '\n', y1[19])
elif inp == 'Valga':
    print(y2, '\n', y1[20])
elif inp == 'Viljandi':
    print(y2, '\n', y1[21])
elif inp == 'Vilsandi':
    print(y2, '\n', y1[22])
elif inp == 'Virtsu':
    print(y2, '\n', y1[23])
elif inp == 'Võru':
    print(y2, '\n', y1[24])
elif inp == 'Väike-Maarja':
    print(y2, '\n', y1[25])
else:
    print('Unsuitable city')
