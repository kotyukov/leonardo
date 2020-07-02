from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import select_operation_callback

operation_ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Смайлификация :)", callback_data=select_operation_callback.new(type='smile')),
            InlineKeyboardButton(text="Перенос стиля", callback_data=select_operation_callback.new(type='nst')),
        ],
        [
            InlineKeyboardButton(text="Далее", callback_data="ignore_me")
        ],
        [
            InlineKeyboardButton(text="Справка", callback_data="intro_help")
        ]
    ]
)

operation_gan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Смайлификация :)", callback_data="ignore_me"),
            InlineKeyboardButton(text="Перенос стиля", callback_data=select_operation_callback.new(type='nst')),
        ],
        [
            InlineKeyboardButton(text="Далее", callback_data="accept_gan")
        ],
        [
            InlineKeyboardButton(text="Справка", callback_data="intro_help")
        ]
    ]
)

operation_nst = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Смайлификация :)", callback_data=select_operation_callback.new(type='smile')),
            InlineKeyboardButton(text="✅ Перенос стиля", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Далее", callback_data="accept_nst")
        ],
        [
            InlineKeyboardButton(text="Справка", callback_data="intro_help")
        ]
    ]
)
