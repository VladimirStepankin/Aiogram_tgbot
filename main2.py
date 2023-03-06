# Inline клавиатура
from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile, Message
from keybords import kb, ikb
import random
from glob import glob
import os
from PIL import Image

from Config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/start
/help
/description
/give
"""

arr_images = glob('images/*')


async def on_startup(_):  # сообщеение в терминале о запуске бота
    print('Бот был успешно запущен')


@dp.message_handler(commands=['start'])
async def links_command(message: types.Message):
    await message.answer(text="Добро пожаловать в главное меню",
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    photo = open(random.choice(arr_images), 'rb')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         caption='Как фото?',
                         reply_markup=ikb)
    await message.delete()


@dp.message_handler(Text(equals='Рандомное фото'))
async def rendom_photo_command(message: types.Message):
    photo = open(random.choice(arr_images), 'rb')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         caption='Вот ваше фото!!!',
                         reply_markup=kb)

    await message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='Огонь!!!')
    await callback.answer(text='Жаль(')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
