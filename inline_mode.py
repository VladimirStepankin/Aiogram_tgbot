from aiogram import Dispatcher, executor, Bot, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib
from keybords import inline_keybord, cb
from Config import TOKEN_API

bot = Bot(TOKEN_API)
db = Dispatcher(bot)


@db.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'Wellcome to my Bot',
                         reply_markup=inline_keybord())


@db.callback_query_handler(cb.filter(action='push_1'))
async def push_first_cb_hendler(callback: types.CallbackQuery):
    await callback.answer('Hello!')


@db.callback_query_handler(cb.filter(action='push_2'))
async def push_second_cb_hendler(callback: types.CallbackQuery):
    await callback.answer('World!')


@db.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or 'Echo!!!'
    input_content = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title=text
    )
    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)

if __name__ == "__main__":
    executor.start_polling(dispatcher=db, skip_updates=True)
