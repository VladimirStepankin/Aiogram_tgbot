from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️ ',
                           callback_data="like",)
ib2 = InlineKeyboardButton(text='👎 ',
                           callback_data="dislike")
ib3 = InlineKeyboardButton(text='Следующее фото',
                           callback_data="next",)
ikb.add(ib1,ib2).add(ib3)


kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton(text='/vote')
b2 = KeyboardButton(text='/help')
b3 = KeyboardButton(text='Рандомное фото')
kb.add(b1, b2).add(b3)