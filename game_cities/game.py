import random


def get_letters():
    l = [chr(i) for i in range(1072, 1072 + 32)]
    l.append('ё')
    l.remove('ь')
    l.remove('ъ')
    return l


class Game:

    def __init__(self):
        self.letters = get_letters()
        self.cities_all = self.get_cities_to_game()
        self.cities_used = {e: [] for e in self.letters}
        self.bot_last_city = ''
        self.user_last_city = ''

    def get_first_city(self):
        random_letter = random.choice(self.letters)
        city = random.choice(self.cities_all[random_letter])
        self.cities_all[random_letter].remove(city)
        self.cities_used[random_letter].append(city)
        self.bot_last_city = city
        return city

    def is_right_city(self, city: str):
        city = city.split(' ')[0]
        first_letter = city[0].lower()
        last_letter = self.bot_last_city[-1] if self.bot_last_city[-1] != 'ь' else self.bot_last_city[-2]
        return last_letter == first_letter

    def is_real_city(self, city: str):
        city = city.split(' ')[0]
        first_letter = city[0].lower()
        if first_letter in self.letters:
            return city in self.cities_all[first_letter] or city in self.cities_used[first_letter]
        return False

    def was_city_used(self, city: str):
        city = city.split(' ')[0]
        first_letter = city[0].lower()
        if city in self.cities_used[first_letter]:
            return True
        else:
            self.cities_all[first_letter].remove(city)
            return False

    def get_no_used_city(self):
        first_letter_user_city = self.user_last_city[0].lower()
        self.cities_used[first_letter_user_city].append(self.user_last_city)
        first_letter = self.user_last_city[-1] if self.user_last_city[-1] != 'ь' else self.user_last_city[-2]
        city = random.choice(self.cities_all[first_letter])
        self.cities_all[first_letter].remove(city)
        self.cities_used[first_letter].append(city)
        self.bot_last_city = city
        return city

    def get_cities_to_game(self):
        cities = {}
        for e in self.letters:
            with open(f'game_cities\\cities\\{e}.txt', 'r', encoding='utf-8') as file:
                resp = file.read().split(' ')
                cities[e] = resp
        return cities

