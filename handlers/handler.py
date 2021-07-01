from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from keyboards.default.keyboard import choice
from loader import dp
import logging
from weather import weather_handler
from game_cities import game_handler


@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, ты написал: {message.text}. \n" \
           f"Пока я умею только играть в города и показывать погоду, выбери что ты хочешь."
    await message.answer(text, reply_markup=choice)

@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, ты написал: {message.text}. \n" \
           f"Пока я умею только играть в города и показывать погоду, выбери что ты хочешь."
    await message.answer(text, reply_markup=choice)