


#
#
#
#
#
#  DEPRECATED
#
#
#
#
#
#






from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import select_resolution_callback


image_resolution_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Demo", callback_data="ignore_me"),
            InlineKeyboardButton(text="Standart", callback_data=select_resolution_callback.new(resolution=400)),
            InlineKeyboardButton(text="Maximal", callback_data=select_resolution_callback.new(resolution=600)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_resolution")
        ]
    ]
)

image_resolution_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Demo", callback_data=select_resolution_callback.new(resolution=250)),
            InlineKeyboardButton(text="✅ Standart", callback_data="ignore_me"),
            InlineKeyboardButton(text="Maximal", callback_data=select_resolution_callback.new(resolution=600)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_resolution")
        ]
    ]
)

image_resolution_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Demo", callback_data=select_resolution_callback.new(resolution=250)),
            InlineKeyboardButton(text="Standart", callback_data=select_resolution_callback.new(resolution=400)),
            InlineKeyboardButton(text="✅ Maximal", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_resolution")
        ]
    ]
)