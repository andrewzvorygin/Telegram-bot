import requests
link = 'https://geodzen.com/cities?'
response = requests.get(link).text
print(response)
#
cities = {}

for e in range(1040, 1040+32):
    cities[chr(e)] = list()
cities['Ё'] = list()

