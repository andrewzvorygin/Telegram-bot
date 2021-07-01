from aiogram.types import Message, CallbackQuery
from .keyboard import choice_end_game
from loader import dp
import logging
from states.state import Test
from game_cities import Game
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text_contains="game", state=None)
async def start_game(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await Test.Game.set()
    game = Game()
    await state.update_data(game=game)
    logging.info(f'Переведено в состояние игры')
    first_city = game.get_first_city()
    next_letter = first_city[-1] if first_city[-1] != 'ь' else first_city[-2]
    answer = f'<b>{first_city}</b>. Тебе на <b>{next_letter.upper()}</b>'
    logging.info(f'первый город: {first_city}')
    await call.message.answer(answer, reply_markup=choice_end_game)
    logging.info(f'Первый город отправлен пользователю')


@dp.message_handler(state=Test.Game)
async def next_city(message: Message, state: FSMContext):
    logging.info('Зашли в метод следующего города')
    city_user = message.text
    data = await state.get_data()
    game = data.get('game')

    if game.is_real_city(city_user):
        if game.was_city_used(city_user):
            await message.answer('Этот город уже называли', reply_markup=choice_end_game)
        else:

            if game.is_right_city(city_user):
                game.user_last_city = city_user
                city_bot = game.get_no_used_city()
                answer = f'<b>{city_bot}</b>. Тебе на <b>{city_bot[-1].upper()}</b>'
                await message.answer(answer, reply_markup=choice_end_game)
            else:
                await message.answer('Этот город не на нужную букву', reply_markup=choice_end_game)

    else:
        await message.answer('Такого города не сущестувует или вы опечатались, попробуйте ещё раз :)',
                             reply_markup=choice_end_game)
    await state.update_data(game=game)


@dp.callback_query_handler(text_contains="end_game", state=Test.Game)
async def finish_game_city(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await state.finish()
    await call.message.answer('Игра окончена')
    logging.info('Игра окончена')
