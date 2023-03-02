from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


from Config import TOKEN_API


#Клавиатура            размер                      сворачивание клавиатуры   
kb=ReplyKeyboardMarkup(resize_keyboard=True)  #, one_time_keyboard=True)
button1 = KeyboardButton('/help')
button2 = KeyboardButton('/description')
button3 = KeyboardButton('/give')
button4 = KeyboardButton('/photo')
kb.add(button1).insert(button2).add(button3).insert(button4)

HELP_COMMAND = """
/start
/help
/description
/give
<b>/photo</b> - <em>Получи картинку</em>
"""


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):  # сообщеение в терминале о запуске бота
    print('Бот был успешно запущен')


@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    # parse_mode = "HTML" меняет отображение текста
    # <em> - курсив
    # <b> - жирный
    # <>
    await message.answer("<em>Добро пожаловать в наш Телеграмм-бот!</em>", 
                         parse_mode="HTML",
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.message):
    await bot.send_message(chat_id=message.from_user.id,  # отправляем в личку список команд
                           text=HELP_COMMAND,
                           parse_mode="HTML")
                           #reply_markup=ReplyKeyboardRemove()) #убирается клавиатура после выбора команды
    await message.delete()


@dp.message_handler(commands=['description'])
async def start_command(message: types.message):
    await message.answer(text="Информация о боте")
    await message.delete()


@dp.message_handler(commands=['give'])
async def sticker(message: types.message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEH9xlkAAGVrbMY7hKFljiUpLrWWLAGM7YAAvcAA1advQoLciQdSPQNMC4E")


# @dp.message_handler()  # эхо с эмоджи
# async def send_emoji(message: types.message):
#     await message.reply(message.text + '🤯 ')


@dp.message_handler(commands=['photo'])
async def send_image(message: types.message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://yandex.ru/images/search?pos=8&from=tabbar&img_url=http%3A%2F%2Fpic.rutubelist.ru%2Fvideo%2F8a%2Feb%2F8aeb27d41a4d0dac9af3f2cf0a9b51a3.jpg&text=%D1%83%D1%82%D0%BA%D0%B8&rpt=simage&lr=119406")
    await message.delete()


@dp.message_handler(commands=['location'])
async def show_location(message: types.message):
    await bot.send_message(chat_id=message.from_user.id,
                           latitude=55,
                           longitude=65)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
                                    # ↑ пропускает команды от пользователя, если бот не был запущен
