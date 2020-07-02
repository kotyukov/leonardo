from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import select_demo_callback

demo_content_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ 1", callback_data="ignore_me"),
            InlineKeyboardButton(text="2", callback_data=select_demo_callback.new(type='content', number=2)),
            InlineKeyboardButton(text="3", callback_data=select_demo_callback.new(type='content', number=3)),
            InlineKeyboardButton(text="4 >", callback_data=select_demo_callback.new(type='content', number=4)),
            InlineKeyboardButton(text="6 >>", callback_data=select_demo_callback.new(type='content', number=6)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_content")
        ]
    ]
)

demo_content_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data=select_demo_callback.new(type='content', number=1)),
            InlineKeyboardButton(text="✅ 2", callback_data="ignore_me"),
            InlineKeyboardButton(text="3", callback_data=select_demo_callback.new(type='content', number=3)),
            InlineKeyboardButton(text="4 >", callback_data=select_demo_callback.new(type='content', number=4)),
            InlineKeyboardButton(text="6 >>", callback_data=select_demo_callback.new(type='content', number=6)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_content")
        ]
    ]
)

demo_content_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data=select_demo_callback.new(type='content', number=1)),
            InlineKeyboardButton(text="2", callback_data=select_demo_callback.new(type='content', number=2)),
            InlineKeyboardButton(text="✅ 3", callback_data="ignore_me"),
            InlineKeyboardButton(text="4 >", callback_data=select_demo_callback.new(type='content', number=4)),
            InlineKeyboardButton(text="6 >>", callback_data=select_demo_callback.new(type='content', number=6)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_content")
        ]
    ]
)

demo_content_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='content', number=1)),
            InlineKeyboardButton(text="< 3", callback_data=select_demo_callback.new(type='content', number=3)),
            InlineKeyboardButton(text="✅ 4", callback_data="ignore_me"),
            InlineKeyboardButton(text="5 >", callback_data=select_demo_callback.new(type='content', number=5)),
            InlineKeyboardButton(text="6 >>", callback_data=select_demo_callback.new(type='content', number=6)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_content")
        ]
    ]
)

demo_content_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='content', number=1)),
            InlineKeyboardButton(text="< 3", callback_data=select_demo_callback.new(type='content', number=3)),
            InlineKeyboardButton(text="4", callback_data=select_demo_callback.new(type='content', number=4)),
            InlineKeyboardButton(text="✅ 5", callback_data="ignore_me"),
            InlineKeyboardButton(text="6", callback_data=select_demo_callback.new(type='content', number=6)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_content")
        ]
    ]
)

demo_content_6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< 1", callback_data=select_demo_callback.new(type='content', number=1)),
            InlineKeyboardButton(text="< 3", callback_data=select_demo_callback.new(type='content', number=3)),
            InlineKeyboardButton(text="4", callback_data=select_demo_callback.new(type='content', number=4)),
            InlineKeyboardButton(text="5", callback_data=select_demo_callback.new(type='content', number=5)),
            InlineKeyboardButton(text="✅ 6", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_content")
        ]
    ]
)
