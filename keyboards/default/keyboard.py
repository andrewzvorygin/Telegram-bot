from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(row_width=2)
weather = InlineKeyboardButton(text="Я хочу узнать погоду", callback_data='weather')
choice.insert(weather)

game = InlineKeyboardButton(text="Я хочу поиграть в города", callback_data="game")
choice.insert(game)



