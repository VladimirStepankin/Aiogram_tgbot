from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData


cb = CallbackData('inline_kb', 'action')


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️ ',
                           callback_data="like",)
ib2 = InlineKeyboardButton(text='👎 ',
                           callback_data="dislike")
ib3 = InlineKeyboardButton(text='Следующее фото',
                           callback_data="next",)
ib4 = InlineKeyboardButton(text='Главное меню',
                           callback_data="main_menu",)
ikb.add(ib1,ib2).add(ib3).add(ib4)


kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton(text='/vote')
b2 = KeyboardButton(text='/help')
b3 = KeyboardButton(text='Рандомное фото')
kb.add(b1, b2).add(b3)

def inline_keybord():
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Button_1', callback_data=cb.new('push_1'))],
        [InlineKeyboardButton('Button_2', callback_data=cb.new('push_2'))],
    ])
    return inline_kb

def get_inline_keybord():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Increase', callback_data='btn_increase'),
        InlineKeyboardButton('Decrease',callback_data='btn_decrease')],
    ])
    return ikb