from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️ ',
                           callback_data="like",)
ib2 = InlineKeyboardButton(text='👎 ',
                           callback_data="dislike")
ikb.add(ib1).insert(ib2)


kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton(text='/vote')
b2 = KeyboardButton(text='/help')
kb.add(b1, b2)