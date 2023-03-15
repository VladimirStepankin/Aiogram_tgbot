"The callback data count"

from aiogram import Dispatcher, executor, Bot, types
from aiogram.utils.exceptions import BotBlocked
import asyncio
from keybords import get_inline_keybord
from Config import TOKEN_API

bot = Bot(TOKEN_API)
db = Dispatcher(bot)
number = 0


@db.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await asyncio.sleep(10)
    await message.answer(f'The current number is {number}',
                         reply_markup=get_inline_keybord())


@db.errors_handler(exception=BotBlocked)
async def error_bot_blocked_handler(update: types.Update, exception: BotBlocked):
    print('Нас заблокировали')
    return True

@db.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def ikb_cb_handler(callback: types.CallbackQuery):
    global number
    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(f'The current number is {number}',
                                         reply_markup=get_inline_keybord())
    elif callback.data == 'btn_decrease':
        number -= 1
        await callback.message.edit_text(f'The current number is {number}',
                                         reply_markup=get_inline_keybord())
    else:
        1/0

if __name__ == "__main__":
    executor.start_polling(dispatcher=db, skip_updates=True)
