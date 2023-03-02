from aiogram import Bot, executor, Dispatcher, types
from Config import TOKEN_API

HELP_COMMAND = """
/start
/help
/description
/give
"""


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот был успешно запущен')


@dp.message_handler(commands=['description'])
async def start_command(massage: types.message):
    await massage.answer(text="Информация о боте")
    await massage.delete()


@dp.message_handler(commands=['start'])
async def start_command(massage: types.message):
    # parse_mode = "HTML" меняет отображение текста
    #<em> - курсив
    #<b> - жирный
    #<>
    await massage.answer("<em>Добро пожаловать в наш Телеграмм-бот!</em>", parse_mode="HTML")
    await massage.delete()


@dp.message_handler(commands=['help'])
async def help_command(massage: types.message):
    await massage.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['give'])
async def sticker(message: types.message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEH9xlkAAGVrbMY7hKFljiUpLrWWLAGM7YAAvcAA1advQoLciQdSPQNMC4E")


# @dp.message_handler()  # эхо с эмоджи
# async def send_emoji(message: types.message):
#     await message.reply(message.text + '🤯 ')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
