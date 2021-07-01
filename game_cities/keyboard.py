from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_end_game = InlineKeyboardMarkup(row_width=1)
end_game = InlineKeyboardButton(text="Я хочу закончить игру", callback_data="end_game")
choice_end_game.insert(end_game)
