from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import select_settings_callback


resolution_epoch_250_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Demo", callback_data="ignore_me"),
            InlineKeyboardButton(text="Standart", callback_data=select_settings_callback.new(resolution=400, epoch=5)),
            InlineKeyboardButton(text="Maximal", callback_data=select_settings_callback.new(resolution=600, epoch=5)),
        ],
        [
            InlineKeyboardButton(text="✅ 5 шагов", callback_data="ignore_me"),
            InlineKeyboardButton(text="10 шагов", callback_data=select_settings_callback.new(resolution=250, epoch=10)),
            InlineKeyboardButton(text="15 шагов", callback_data=select_settings_callback.new(resolution=250, epoch=15)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)

resolution_epoch_400_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Demo", callback_data=select_settings_callback.new(resolution=250, epoch=5)),
            InlineKeyboardButton(text="✅ Standart", callback_data="ignore_me"),
            InlineKeyboardButton(text="Maximal", callback_data=select_settings_callback.new(resolution=600, epoch=5)),
        ],
        [
            InlineKeyboardButton(text="✅ 5 шагов", callback_data="ignore_me"),
            InlineKeyboardButton(text="10 шагов", callback_data=select_settings_callback.new(resolution=400, epoch=10)),
            InlineKeyboardButton(text="15 шагов", callback_data=select_settings_callback.new(resolution=400, epoch=15)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)

resolution_epoch_600_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Demo", callback_data=select_settings_callback.new(resolution=250, epoch=5)),
            InlineKeyboardButton(text="Standart", callback_data=select_settings_callback.new(resolution=400, epoch=5)),
            InlineKeyboardButton(text="✅ Maximal", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="✅ 5 шагов", callback_data="ignore_me"),
            InlineKeyboardButton(text="10 шагов", callback_data=select_settings_callback.new(resolution=600, epoch=10)),
            InlineKeyboardButton(text="15 шагов", callback_data=select_settings_callback.new(resolution=600, epoch=15)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)

resolution_epoch_250_10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Demo", callback_data="ignore_me"),
            InlineKeyboardButton(text="Standart", callback_data=select_settings_callback.new(resolution=400, epoch=10)),
            InlineKeyboardButton(text="Maximal", callback_data=select_settings_callback.new(resolution=600, epoch=10)),
        ],
        [
            InlineKeyboardButton(text="5 шагов", callback_data=select_settings_callback.new(resolution=250, epoch=5)),
            InlineKeyboardButton(text="✅ 10 шагов", callback_data="ignore_me"),
            InlineKeyboardButton(text="15 шагов", callback_data=select_settings_callback.new(resolution=250, epoch=15)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)

resolution_epoch_400_10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Demo", callback_data=select_settings_callback.new(resolution=250, epoch=10)),
            InlineKeyboardButton(text="✅ Standart", callback_data="ignore_me"),
            InlineKeyboardButton(text="Maximal", callback_data=select_settings_callback.new(resolution=600, epoch=10)),
        ],
        [
            InlineKeyboardButton(text="5 шагов", callback_data=select_settings_callback.new(resolution=400, epoch=5)),
            InlineKeyboardButton(text="✅ 10 шагов", callback_data="ignore_me"),
            InlineKeyboardButton(text="15 шагов", callback_data=select_settings_callback.new(resolution=400, epoch=15)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)

resolution_epoch_600_10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Demo", callback_data=select_settings_callback.new(resolution=250, epoch=10)),
            InlineKeyboardButton(text="Standart", callback_data=select_settings_callback.new(resolution=400, epoch=10)),
            InlineKeyboardButton(text="✅ Maximal", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="5 шагов", callback_data=select_settings_callback.new(resolution=600, epoch=5)),
            InlineKeyboardButton(text="✅ 10 шагов", callback_data="ignore_me"),
            InlineKeyboardButton(text="15 шагов", callback_data=select_settings_callback.new(resolution=600, epoch=15)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)

resolution_epoch_250_15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Demo", callback_data="ignore_me"),
            InlineKeyboardButton(text="Standart", callback_data=select_settings_callback.new(resolution=400, epoch=15)),
            InlineKeyboardButton(text="Maximal", callback_data=select_settings_callback.new(resolution=600, epoch=15)),
        ],
        [
            InlineKeyboardButton(text="5 шагов", callback_data=select_settings_callback.new(resolution=250, epoch=5)),
            InlineKeyboardButton(text="10 шагов", callback_data=select_settings_callback.new(resolution=250, epoch=10)),
            InlineKeyboardButton(text="✅ 15 шагов", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)

resolution_epoch_400_15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Demo", callback_data=select_settings_callback.new(resolution=250, epoch=15)),
            InlineKeyboardButton(text="✅ Standart", callback_data="ignore_me"),
            InlineKeyboardButton(text="Maximal", callback_data=select_settings_callback.new(resolution=600, epoch=15)),
        ],
        [
            InlineKeyboardButton(text="5 шагов", callback_data=select_settings_callback.new(resolution=400, epoch=5)),
            InlineKeyboardButton(text="10 шагов", callback_data=select_settings_callback.new(resolution=400, epoch=10)),
            InlineKeyboardButton(text="✅ 15 шагов", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)

resolution_epoch_600_15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Demo", callback_data=select_settings_callback.new(resolution=250, epoch=15)),
            InlineKeyboardButton(text="Standart", callback_data=select_settings_callback.new(resolution=400, epoch=15)),
            InlineKeyboardButton(text="✅ Maximal", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="5 шагов", callback_data=select_settings_callback.new(resolution=600, epoch=5)),
            InlineKeyboardButton(text="10 шагов", callback_data=select_settings_callback.new(resolution=600, epoch=10)),
            InlineKeyboardButton(text="✅ 15 шагов", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_settings")
        ]
    ]
)