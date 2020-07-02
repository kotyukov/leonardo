from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import select_quantity_callback

select_style_quantity_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ 1 стиль", callback_data="ignore_me"),
            InlineKeyboardButton(text="2 стиля", callback_data=select_quantity_callback.new(quantity=2)),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_quantity")
        ]
    ]
)

select_style_quantity_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1 стиль", callback_data=select_quantity_callback.new(quantity=1)),
            InlineKeyboardButton(text="✅ 2 стиля", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="accept_quantity")
        ]
    ]
)