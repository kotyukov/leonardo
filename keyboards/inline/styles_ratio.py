from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import select_ratio_callback

styles_ratio_1090 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ 10/90", callback_data="ignore_me"),
            InlineKeyboardButton(text="30/70", callback_data=select_ratio_callback.new(action='set_ratio', ratio='30_70')),
            InlineKeyboardButton(text="50/50", callback_data=select_ratio_callback.new(action='set_ratio', ratio='50_50')),
            InlineKeyboardButton(text="70/30", callback_data=select_ratio_callback.new(action='set_ratio', ratio='70_30')),
            InlineKeyboardButton(text="90/10", callback_data=select_ratio_callback.new(action='set_ratio', ratio='90_10')),
        ],
        [
            InlineKeyboardButton(text="Принять", callback_data="accept_ratio")
        ]
    ]
)

styles_ratio_3070 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="10/90", callback_data=select_ratio_callback.new(action='set_ratio', ratio='10_90')),
            InlineKeyboardButton(text="✅ 30/70", callback_data="ignore_me"),
            InlineKeyboardButton(text="50/50", callback_data=select_ratio_callback.new(action='set_ratio', ratio='50_50')),
            InlineKeyboardButton(text="70/30", callback_data=select_ratio_callback.new(action='set_ratio', ratio='70_30')),
            InlineKeyboardButton(text="90/10", callback_data=select_ratio_callback.new(action='set_ratio', ratio='90_10')),
        ],
        [
            InlineKeyboardButton(text="Принять", callback_data="accept_ratio")
        ]
    ]
)

styles_ratio_5050 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="10/90", callback_data=select_ratio_callback.new(action='set_ratio', ratio='10_90')),
            InlineKeyboardButton(text="30/70", callback_data=select_ratio_callback.new(action='set_ratio', ratio='30_70')),
            InlineKeyboardButton(text="✅ 50/50", callback_data="ignore_me"),
            InlineKeyboardButton(text="70/30", callback_data=select_ratio_callback.new(action='set_ratio', ratio='70_30')),
            InlineKeyboardButton(text="90/10", callback_data=select_ratio_callback.new(action='set_ratio', ratio='90_10')),
        ],
        [
            InlineKeyboardButton(text="Принять", callback_data="accept_ratio")
        ]
    ]
)

styles_ratio_7030 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="10/90", callback_data=select_ratio_callback.new(action='set_ratio', ratio='10_90')),
            InlineKeyboardButton(text="30/70", callback_data=select_ratio_callback.new(action='set_ratio', ratio='30_70')),
            InlineKeyboardButton(text="50/50", callback_data=select_ratio_callback.new(action='set_ratio', ratio='50_50')),
            InlineKeyboardButton(text="✅ 70/30", callback_data="ignore_me"),
            InlineKeyboardButton(text="90/10", callback_data=select_ratio_callback.new(action='set_ratio', ratio='90_10')),
        ],
        [
            InlineKeyboardButton(text="Принять", callback_data="accept_ratio")
        ]
    ]
)

styles_ratio_9010 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="10/90", callback_data=select_ratio_callback.new(action='set_ratio', ratio='10_90')),
            InlineKeyboardButton(text="30/70", callback_data=select_ratio_callback.new(action='set_ratio', ratio='30_70')),
            InlineKeyboardButton(text="50/50", callback_data=select_ratio_callback.new(action='set_ratio', ratio='50_50')),
            InlineKeyboardButton(text="70/30", callback_data=select_ratio_callback.new(action='set_ratio', ratio='70_30')),
            InlineKeyboardButton(text="✅ 90/10", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Принять", callback_data="accept_ratio")
        ]
    ]
)
