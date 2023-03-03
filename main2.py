# Inline клавиатура
from aiogram import Bot, executor, Dispatcher, types
from keybords import kb, ikb


from Config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):  # сообщеение в терминале о запуске бота
    print('Бот был успешно запущен')


@dp.message_handler(commands=['start'])
async def links_command(message: types.message):
    await message.answer(text="Добро пожаловать в главное меню",
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://thumbs.dreamstime.com/b/beautiful-rain-forest-ang-ka-nature-trail-doi-inthanon-national-park-thailand-36703721.jpg",
                         caption='Как фото?',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='Огонь!!!')
    await callback.answer(text='Жаль(')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
