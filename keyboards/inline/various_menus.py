from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Поехали!", callback_data='start_dialogue'),
        ]
    ]
)

smile_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)

to_examples_list_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data='to_examples_list'),
        ]
    ]
)

help_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Смайлификация", callback_data='example_smile'),
            InlineKeyboardButton(text="Перенос 1 стиля", callback_data='example_nst_one'),
            InlineKeyboardButton(text="Перенос 2 стилей", callback_data='example_nst_two'),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)

next_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Далее", callback_data='accept_uploaded_img'),
        ]
    ]
)

run_nst_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад к настройкам", callback_data="back_to_settings"),
            InlineKeyboardButton(text="В начало", callback_data="reset_all")
        ],
        [
            InlineKeyboardButton(text="Поехали!", callback_data="run_transfer")
        ]
    ]
)