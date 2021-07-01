from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_thank = InlineKeyboardMarkup(row_width=1)
end_game = InlineKeyboardButton(text="Спасибо", callback_data="thank")
choice_thank.insert(end_game)
