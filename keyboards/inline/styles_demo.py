from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import select_demo_callback

demo_style_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ 1", callback_data="ignore_me"),
            InlineKeyboardButton(text="2", callback_data=select_demo_callback.new(type='style', number=2)),
            InlineKeyboardButton(text="3", callback_data=select_demo_callback.new(type='style', number=3)),
            InlineKeyboardButton(text="4 >", callback_data=select_demo_callback.new(type='style', number=4)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="✅ 2", callback_data="ignore_me"),
            InlineKeyboardButton(text="3", callback_data=select_demo_callback.new(type='style', number=3)),
            InlineKeyboardButton(text="4 >", callback_data=select_demo_callback.new(type='style', number=4)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="2", callback_data=select_demo_callback.new(type='style', number=2)),
            InlineKeyboardButton(text="✅ 3", callback_data="ignore_me"),
            InlineKeyboardButton(text="4 >", callback_data=select_demo_callback.new(type='style', number=4)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 3", callback_data=select_demo_callback.new(type='style', number=3)),
            InlineKeyboardButton(text="✅ 4", callback_data="ignore_me"),
            InlineKeyboardButton(text="5 >", callback_data=select_demo_callback.new(type='style', number=5)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 4", callback_data=select_demo_callback.new(type='style', number=4)),
            InlineKeyboardButton(text="✅ 5", callback_data="ignore_me"),
            InlineKeyboardButton(text="6 >", callback_data=select_demo_callback.new(type='style', number=6)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 5", callback_data=select_demo_callback.new(type='style', number=5)),
            InlineKeyboardButton(text="✅ 6", callback_data="ignore_me"),
            InlineKeyboardButton(text="7 >", callback_data=select_demo_callback.new(type='style', number=7)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 6", callback_data=select_demo_callback.new(type='style', number=6)),
            InlineKeyboardButton(text="✅ 7", callback_data="ignore_me"),
            InlineKeyboardButton(text="8 >", callback_data=select_demo_callback.new(type='style', number=8)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 7", callback_data=select_demo_callback.new(type='style', number=7)),
            InlineKeyboardButton(text="✅ 8", callback_data="ignore_me"),
            InlineKeyboardButton(text="9 >", callback_data=select_demo_callback.new(type='style', number=9)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 8", callback_data=select_demo_callback.new(type='style', number=8)),
            InlineKeyboardButton(text="✅ 9", callback_data="ignore_me"),
            InlineKeyboardButton(text="10 >", callback_data=select_demo_callback.new(type='style', number=10)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 9", callback_data=select_demo_callback.new(type='style', number=9)),
            InlineKeyboardButton(text="✅ 10", callback_data="ignore_me"),
            InlineKeyboardButton(text="11 >", callback_data=select_demo_callback.new(type='style', number=11)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 10", callback_data=select_demo_callback.new(type='style', number=10)),
            InlineKeyboardButton(text="✅ 11", callback_data="ignore_me"),
            InlineKeyboardButton(text="12 >", callback_data=select_demo_callback.new(type='style', number=12)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 10", callback_data=select_demo_callback.new(type='style', number=10)),
            InlineKeyboardButton(text="✅ 11", callback_data="ignore_me"),
            InlineKeyboardButton(text="12 >", callback_data=select_demo_callback.new(type='style', number=12)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_12 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 11", callback_data=select_demo_callback.new(type='style', number=11)),
            InlineKeyboardButton(text="✅ 12", callback_data="ignore_me"),
            InlineKeyboardButton(text="13 >", callback_data=select_demo_callback.new(type='style', number=13)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_13 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 12", callback_data=select_demo_callback.new(type='style', number=12)),
            InlineKeyboardButton(text="✅ 13", callback_data="ignore_me"),
            InlineKeyboardButton(text="14 >", callback_data=select_demo_callback.new(type='style', number=14)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_14 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 13", callback_data=select_demo_callback.new(type='style', number=13)),
            InlineKeyboardButton(text="✅ 14", callback_data="ignore_me"),
            InlineKeyboardButton(text="15 >", callback_data=select_demo_callback.new(type='style', number=15)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 14", callback_data=select_demo_callback.new(type='style', number=14)),
            InlineKeyboardButton(text="✅ 15", callback_data="ignore_me"),
            InlineKeyboardButton(text="16 >", callback_data=select_demo_callback.new(type='style', number=16)),
            InlineKeyboardButton(text="18 >>", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_16 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 15", callback_data=select_demo_callback.new(type='style', number=15)),
            InlineKeyboardButton(text="✅ 16", callback_data="ignore_me"),
            InlineKeyboardButton(text="17", callback_data=select_demo_callback.new(type='style', number=17)),
            InlineKeyboardButton(text="18", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_17 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 15", callback_data=select_demo_callback.new(type='style', number=15)),
            InlineKeyboardButton(text="16", callback_data=select_demo_callback.new(type='style', number=16)),
            InlineKeyboardButton(text="✅ 17", callback_data="ignore_me"),
            InlineKeyboardButton(text="18", callback_data=select_demo_callback.new(type='style', number=18)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)

demo_style_18 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='style', number=1)),
            InlineKeyboardButton(text="< 15", callback_data=select_demo_callback.new(type='style', number=15)),
            InlineKeyboardButton(text="16", callback_data=select_demo_callback.new(type='style', number=16)),
            InlineKeyboardButton(text="17", callback_data=select_demo_callback.new(type='style', number=17)),
            InlineKeyboardButton(text="✅ 18", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_style")
        ]
    ]
)
