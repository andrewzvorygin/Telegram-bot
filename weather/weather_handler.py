from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import dp
import logging
from .keyboard import choice_thank
from states.state import Test


@dp.callback_query_handler(text_contains="weather", state=None)
async def get_city_to_weather(call: CallbackQuery):
    await call.answer(cache_time=60)
    await Test.Weather.set()
    await call.message.answer('В каком городе вы хотите узнать погоду?\n')


@dp.message_handler(state=Test.Weather)
async def choosing_city_weather(message: Message):
    logging.info('Зашли в метод выбора города погоды')
    city_user = message.text
    await message.answer(f'Вы выбрали город {city_user}', reply_markup=choice_thank)


@dp.callback_query_handler(text_contains="thank", state=Test.Weather)
async def finish_game_city(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await state.finish()
    await call.message.answer('Обращайтесь, но не часто :)')
    logging.info('Выход из состояния прогноза погоды')
