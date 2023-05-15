# Homowork 1
import requests
from pprint import pprint

url = 'https://akabab.github.io/superhero-api/api'
routes = '/all.json'
resp = requests.get(url+routes).json()
heroes = {}
for row in resp:
    if row['name'] in ('Hulk', 'Captain America', 'Thanos'):
        heroes[row['name']] = row['powerstats']['intelligence']
        #print(row)
sorted_rooms = sorted(heroes.items(), key=lambda item: -item[1])
pprint(f'Самый умный герой - {sorted_rooms[0][0]}')

#Homework 2
from tok import TOKEN
from ya_disk import YandexDisk
yd = YandexDisk(token=TOKEN)
#yd.upload_file_to_disk("Netology homework/test.txt", "test.txt")

#Homework 3
import time
import datetime

date1 = datetime.datetime.now()
date2 = date1 + datetime.timedelta(days=-2)

date_last = int(time.mktime(time.strptime(date1.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')))
date2_first = int(time.mktime(time.strptime(date2.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')))

url = f'https://api.stackexchange.com//2.3/questions'
params = {
    "fromdate": date2_first,
    "todate": date_last,
    "order": "desc",
    "sort": "activity",
    "site": "stackoverflow",
    "tagged": "Python"
}
resp = requests.get(url=url,params=params).json()
print()
print(f"Список вопрос с {date2.strftime('%Y-%m-%d %H:%M:%S')} по {date1.strftime('%Y-%m-%d %H:%M:%S')}")
inti = 1
for item in resp['items']:
    print(f"{inti}. {item['title']}")
    inti += 1
    