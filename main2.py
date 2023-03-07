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

arr_images = glob('images/*')  # список из картинок из папки

dict_img = dict(zip(arr_images, [1, 2, 3, 4, 5]))  # словарь для описаний картинок
random_photo = random.choice(list(dict_img.keys()))





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
    random_photo = random.choice(list(dict_img.keys()))
    # photo = open(random.choice(arr_images), 'rb')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=open(random_photo, 'rb'),
                         caption=dict_img[random_photo],
                         reply_markup=ikb)
    await message.delete()


@dp.message_handler(Text(equals='Рандомное фото'))
async def rendom_photo_command(message: types.Message):
    random_photo = random.choice(list(dict_img.keys()))
    photo = open(random_photo, 'rb')
    await bot.send_photo(chat_id=message.chat.id,
                        photo=photo,  
                        caption=dict_img[random_photo],  # привязка подписи к картинке
                        reply_markup=ikb)
    await message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    global random_photo
    if callback.data == 'like':
        await callback.answer(text='Огонь!!!')
    elif callback.data == 'dislike':
        await callback.answer(text='Жаль(')
    else:
        #await rendom_photo_command(message=callback.message)
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(dict_img.keys()))))
        photo = open(random_photo, 'rb')
        await callback.message.edit_media(types.InputMedia(media=photo,
                                                           type='photo',
                                                           caption=dict_img[random_photo]),
                                        reply_markup=ikb)
        await callback.answer()
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
