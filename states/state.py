from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Weather = State()
    Game = State()
