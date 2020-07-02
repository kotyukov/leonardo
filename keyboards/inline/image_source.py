from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import select_img_source_callback

source_ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Выберу из коллекции", callback_data=select_img_source_callback.new(source='collection')),
            InlineKeyboardButton(text="Загружу самостоятельно", callback_data=select_img_source_callback.new(source='upload_new')),
        ],
        [
            InlineKeyboardButton(text="Далее", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)

source_collection = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Выберу из коллекции", callback_data="ignore_me"),
            InlineKeyboardButton(text="Загружу самостоятельно", callback_data=select_img_source_callback.new(source='upload_new')),
        ],
        [
            InlineKeyboardButton(text="Далее", callback_data="accept_collection_source")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)

source_upload = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Выберу из коллекции", callback_data=select_img_source_callback.new(source='collection')),
            InlineKeyboardButton(text="✅ Загружу самостоятельно", callback_data="ignore_me"),
        ],
        [
            InlineKeyboardButton(text="Далее", callback_data="accept_upload_source")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)