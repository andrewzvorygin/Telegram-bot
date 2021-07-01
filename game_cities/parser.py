import requests
from bs4 import BeautifulSoup


def get_letters():
    l = [chr(i) for i in range(1072, 1072 + 32)]
    l.append('ё')
    l.remove('ь')
    l.remove('ъ')
    return l


letters = get_letters()


link = 'https://geodzen.com/cities?letter='
all_city = {}
all_city_teg = []
path = 'cities'

for letter in letters:
    all_city[letter] = []
    part = 0
    while True:
        response = requests.get(f'{link}{letter}&part={part}').text
        soup = BeautifulSoup(response, 'lxml')
        table = soup.find('table', class_='cities')
        all_city_teg = table.find_all('tr', class_='city')
        if len(all_city_teg) == 0:
            break
        for e in all_city_teg:
            city = e.find('a').text
            all_city[letter].append(city)
        part += 1
    print(all_city[letter])
    with open(f'cities\\{letter}.txt', 'w', encoding='utf-8') as file:
        for city in all_city[letter]:
            file.write(f'{city} ')


