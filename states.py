from aiogram.dispatcher.filters.state import StatesGroup, State


class NSTStates(StatesGroup):
    welcome = State()
    style_gan_selected = State()
    gatys_nst_selected = State()
    content_img_accepted = State()
    quantity_accepted = State()
    style_imgs_accepted = State()
    ready_to_transfer = State()
    in_process = State()