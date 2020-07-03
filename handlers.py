import gc
import os
from datetime import datetime, timedelta

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import (CallbackQuery, InputMediaPhoto, Message,
                           ReplyKeyboardRemove)
from aiogram.types.message import ContentType
from PIL import Image

import torch
import torch.optim as optim
from callback_datas import *
from config import admin_id
from core import *
from keyboards.inline.various_menus import *
from main import bot, dp
from model import GramMatrix, StyleLoss, VGG_nst
from states import NSTStates
from torch.autograd import Variable
from utils import *

# admin_id = os.getenv("admin_id")


# -----------------------
# Обработка ignore_me коллбека
# -----------------------
@dp.callback_query_handler(text='ignore_me', state="*")
async def do_nothing(call: CallbackQuery):
    await call.answer() # Убираем иконку часов с кнопки
    return


# -----------------------
# Обработка текстовой команды /devinfo
# -----------------------
@dp.message_handler(Command("devinfo"))
async def show_devinfo(message: Message, state: FSMContext):
    await message.answer(text=messages['devinfo'])


# -----------------------
# Обработка текстовой команды /start
# -----------------------
@dp.message_handler(Command("start"))
async def send_welcome(message: Message, state: FSMContext):
    await message.answer(text=messages['welcome'], reply_markup=start_menu)
    await NSTStates.welcome.set()


# -----------------------
# Меню: Welcome-сообщение.
# Кнопка: "Поехали!"
# -----------------------
# Меню: Финальное меню.
# Кнопка: "В начало"
# -----------------------
@dp.callback_query_handler(text='start_dialogue', state=NSTStates.welcome)
@dp.callback_query_handler(text='reset_all', state=NSTStates.ready_to_transfer)
async def show_available_operations(call: CallbackQuery, state: FSMContext):
    await NSTStates.welcome.set()
    async with state.proxy() as data:
        data['selected_content'] = '1'
        data['selected_style'] = '1'
        data['wh_content_size'] = ()
        data['selected_operation'] = 'ndf'
        data['selected_content_source'] = 'ndf'
        data['selected_style_source'] = 'ndf'
        data['selected_style_quantity'] = '1'
        data['selected_ratio'] = '50_50'
        data['selected_resolution'] = '250'
        data['selected_epoch'] = '5'
        data['path_to_content'] = 'content_large/content_(1).png'
        data['path_to_style'] = []
        data['number_of_styles_received'] = 0
    selected_operation = await get_from_state('selected_operation', state)
    await call.message.delete()
    await call.message.answer(text=messages['select_operation'], reply_markup=operation_set[selected_operation])
    

# -----------------------
# Меню: Выберите операцию, которую должен проделать бот.
# Кнопки (навигация): "Смайлификация :)", "Перенос стиля"
# -----------------------
@dp.callback_query_handler(select_operation_callback.filter(), state=NSTStates.welcome)
async def set_operation(call: CallbackQuery, callback_data: dict, state: FSMContext):
    operation = callback_data.get("type")
    await call.message.edit_reply_markup(reply_markup=operation_set[operation])
    async with state.proxy() as data:
        data['selected_operation'] = operation
    

# -----------------------
# Меню: Выберите операцию, которую должен проделать бот.
# Кнопка: "Готово" + выбрана "Смайлификация :)"
# -----------------------
@dp.callback_query_handler(text='accept_gan', state=NSTStates.welcome)
async def accept_operation_gan(call: CallbackQuery, state: FSMContext):
    await NSTStates.style_gan_selected.set()
    await call.message.edit_text(text=messages['smilification'], reply_markup=smile_menu)


# -----------------------
# Меню: Смайлификация.
# Кнопка: "Назад"
# -----------------------
# Меню: Чтобы посмотреть примеры результатов работы...
# Кнопка: "Назад"
# -----------------------
# Меню: Вам необходимо предоставить картинку-контент.
# Кнопка: "Назад"
# -----------------------
@dp.callback_query_handler(text='back', state=NSTStates.style_gan_selected)
@dp.callback_query_handler(text='back', state=NSTStates.welcome)
@dp.callback_query_handler(text='back', state=NSTStates.gatys_nst_selected)
async def back_to_operation(call: CallbackQuery, state: FSMContext):
    await NSTStates.welcome.set()
    selected_operation = await get_from_state('selected_operation', state)
    await call.message.edit_text(text=messages['select_operation'], reply_markup=operation_set[selected_operation])


# -----------------------
# Меню: Выберите операцию, которую должен проделать бот.
# Кнопка: "Справка"
# -----------------------
# Меню: Примеры в справке (х3), вывод каждого результата.
# Кнопка: "Назад"
# -----------------------
@dp.callback_query_handler(text='intro_help', state=NSTStates.welcome)
@dp.callback_query_handler(text='to_examples_list', state=NSTStates.welcome)
async def show_help_menu(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text=messages['help_menu'], reply_markup=help_menu)


# -----------------------
# Меню: Чтобы посмотреть примеры результатов работы...
# Кнопка: "Смайлификация"
# -----------------------
@dp.callback_query_handler(text='example_smile', state=NSTStates.welcome)
async def show_smile_example(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer_photo(photo=open(f'examples/example_smilification.png', 'rb'),
                                    caption=messages['example_smile'],
                                    reply_markup=to_examples_list_btn)


# -----------------------
# Меню: Чтобы посмотреть примеры результатов работы...
# Кнопка: "Перенос 1 стиля"
# -----------------------
@dp.callback_query_handler(text='example_nst_one', state=NSTStates.welcome)
async def show_nst_example_one(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer_photo(photo=open('examples/example_transfer_one.png', 'rb'),
                                    caption=messages['example_nst_one'],
                                    reply_markup=to_examples_list_btn)


# -----------------------
# Меню: Чтобы посмотреть примеры результатов работы...
# Кнопка: "Перенос 2 стилей"
# -----------------------
@dp.callback_query_handler(text='example_nst_two', state=NSTStates.welcome)
async def show_nst_example_two(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer_photo(photo=open(f'examples/example_transfer_two.png', 'rb'),
                                    caption=messages['example_nst_two'],
                                    reply_markup=to_examples_list_btn)


# -----------------------
# Меню: Выберите операцию, которую должен проделать бот.
# Кнопка: "Готово" + выбран "Перенос стиля"
# -----------------------
@dp.callback_query_handler(text='accept_nst', state=NSTStates.welcome)
async def accept_operation_nst(call: CallbackQuery, state: FSMContext):
    await NSTStates.gatys_nst_selected.set()
    selected_content_source = await get_from_state('selected_content_source', state)
    await call.message.edit_text(text=messages['select_content'], reply_markup=source_set[selected_content_source])


# -----------------------
# Меню: Вам необходимо предоставить картинку-контент.
# Кнопки (навигация): "Выберу из коллекции", "Загружу собственную"
# -----------------------
@dp.callback_query_handler(select_img_source_callback.filter(), state=NSTStates.gatys_nst_selected)
async def set_content_source(call: CallbackQuery, callback_data: dict, state: FSMContext):
    source = callback_data.get("source")
    await call.message.edit_reply_markup(reply_markup=source_set[source])
    async with state.proxy() as data:
        data['selected_content_source'] = source


# -----------------------
# Меню: Вам необходимо предоставить картинку-контент.
# Кнопка: "Далее" + выбрано "Выберу из коллекции"
# -----------------------
@dp.callback_query_handler(text='accept_collection_source', state=NSTStates.gatys_nst_selected)
async def get_content_from_collection(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    selected_content = await get_from_state('selected_content', state)
    await call.message.answer_photo(photo=open(f'content_demos/demo_({selected_content}).png', 'rb'),
                                    caption=messages['choose_content_pic'],
                                    reply_markup=demo_content_set[selected_content])


# -----------------------
# Меню: Вам необходимо предоставить картинку-контент.
# Кнопка: "Далее" + выбрано "Загружу самостоятельно"
# -----------------------
@dp.callback_query_handler(text='accept_upload_source', state=NSTStates.gatys_nst_selected)
async def waiting_content_from_user(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text=messages['upload_content'])


# -----------------------
# Обработка: Получение от пользователя картинки-контента.
# -----------------------
@dp.message_handler(state=NSTStates.gatys_nst_selected, content_types=ContentType.PHOTO)
async def get_content_from_user(message: Message, state: FSMContext):
    path = f'received_data/content_{message.from_user.id}.jpg'
    async with state.proxy() as data:
        data['path_to_content'] = path
    await message.photo[-1].download(path)
    await NSTStates.content_img_accepted.set()
    await message.answer(text=messages['content_load_succ'], reply_markup=next_btn)


# -----------------------
# Меню: Выберите картинку на которую будет перенесён новый стиль.
# Кнопки (навигация): "1", "2", "3", "4", "5", "6"
# -----------------------
@dp.callback_query_handler(select_demo_callback.filter(type='content'), state=NSTStates.gatys_nst_selected)
async def set_content(call: CallbackQuery, callback_data: dict, state: FSMContext):
    number = callback_data.get("number")
    await call.message.edit_media(media=InputMediaPhoto(open(f'content_demos/demo_({number}).png', 'rb'), caption=messages['choose_content_pic']),
                                  reply_markup=demo_content_set[number])
    async with state.proxy() as data:
        data['selected_content'] = number
        data['path_to_content'] = f'content_large/content_({number}).png'


# -----------------------
# Сообщение: Картинка-контент успешно загружена.
# Кнопка: "Далее"
# -----------------------
# Меню: Выберите картинку на которую будет перенесён новый стиль.
# Кнопка: "Готово"
# -----------------------
@dp.callback_query_handler(text='accept_uploaded_img', state=NSTStates.content_img_accepted)
@dp.callback_query_handler(text='accept_content', state=NSTStates.gatys_nst_selected)
async def accept_content(call: CallbackQuery, state: FSMContext):
    await NSTStates.content_img_accepted.set()
    async with state.proxy() as data:
        content = data['path_to_content']
        data['wh_content_size'] = await get_image_size(content)
    await call.message.delete()
    selected_style_quantity = await get_from_state('selected_style_quantity', state)
    await call.message.answer(text=messages['style_quantity'],
                              reply_markup=style_quantity_set[selected_style_quantity])


# -----------------------
# Меню: Выберите количество стилей для переноса.
# Кнопки (навигация): "1 стиль", "2 стиля"
# -----------------------
@dp.callback_query_handler(select_quantity_callback.filter(), state=NSTStates.content_img_accepted)
async def set_styles_quantity(call: CallbackQuery, callback_data: dict, state: FSMContext):
    quantity = callback_data.get("quantity")
    await call.message.edit_reply_markup(reply_markup=style_quantity_set[quantity])
    async with state.proxy() as data:
        data['selected_style_quantity'] = quantity


# -----------------------
# Меню: Выберите количество стилей для переноса.
# Кнопка: "Готово"
# -----------------------
@dp.callback_query_handler(text='accept_quantity', state=NSTStates.content_img_accepted)
async def accept_quantity(call: CallbackQuery, state: FSMContext):
    await NSTStates.quantity_accepted.set()
    selected_style_source = await get_from_state('selected_style_source', state)
    await call.message.edit_text(text=messages['select_style'], reply_markup=source_set[selected_style_source])


# -----------------------
# Меню: Вам необходимо предоставить картинку-контент.
# Кнопка: "Назад"
# -----------------------
@dp.callback_query_handler(text='back', state=NSTStates.quantity_accepted)
async def back_to_quantity_selection(call: CallbackQuery, state: FSMContext):
    selected_style_quantity = await get_from_state('selected_style_quantity', state)
    await call.message.edit_text(text=messages['style_quantity'],
                                 reply_markup=style_quantity_set[selected_style_quantity])
    await NSTStates.content_img_accepted.set()


# -----------------------
# Меню: Вам необходимо предоставить выбранное количество картинок-стилей.
# Кнопки (навигация): "Выберу из коллекции", "Загружу самостоятельно"
# -----------------------
@dp.callback_query_handler(select_img_source_callback.filter(), state=NSTStates.quantity_accepted)
async def set_style_source(call: CallbackQuery, callback_data: dict, state: FSMContext):
    source = callback_data.get("source")
    await call.message.edit_reply_markup(reply_markup=source_set[source])
    async with state.proxy() as data:
        data['selected_style_source'] = source


# -----------------------
# Меню: Вам необходимо предоставить выбранное количество картинок-стилей.
# Кнопка: "Далее" + выбрано "Выберу из коллекции"
# -----------------------
@dp.callback_query_handler(text='accept_collection_source', state=NSTStates.quantity_accepted)
async def get_style_from_collection(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    selected_style = await get_from_state('selected_style', state)
    await call.message.answer_photo(photo=open(f'style_demos/demo_({selected_style}).png', 'rb'),
                                    caption=messages['choose_style_pic'],
                                    reply_markup=demo_style_set[selected_style])


# -----------------------
# Меню: Вам необходимо предоставить выбранное количество картинок-стилей.
# Кнопка: "Далее" + выбрано "Загружу самостоятельно"
# -----------------------
@dp.callback_query_handler(text='accept_upload_source', state=NSTStates.quantity_accepted)
async def waiting_style_from_user(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text=messages['upload_style'])


# -----------------------
# Обработка: Получение от пользователя картинки-стиля.
# -----------------------
@dp.message_handler(state=NSTStates.quantity_accepted, content_types=ContentType.PHOTO)
async def get_style_from_user(message: Message, state: FSMContext):
    async with state.proxy() as data:
        quantity = data['selected_style_quantity']
        received = data['number_of_styles_received']
        if quantity == '2' and received == 1:
            path = f'received_data/style2_{message.from_user.id}.jpg'
        else:
            path = f'received_data/style_{message.from_user.id}.jpg'
        data['path_to_style'].append(path)
    await message.photo[-1].download(path)
    await message.answer(text=messages['style_load_succ'], reply_markup=next_btn)
    await NSTStates.style_imgs_accepted.set()


# -----------------------
# Меню: Выберите стиль из коллекции.
# Кнопки (навигация): "1" ... "18"
# -----------------------
@dp.callback_query_handler(select_demo_callback.filter(type='style'), state=NSTStates.quantity_accepted)
async def set_style(call: CallbackQuery, callback_data: dict, state: FSMContext):
    number = callback_data.get("number")
    await call.message.edit_media(media=InputMediaPhoto(open(f'style_demos/demo_({number}).png', 'rb'),
                                  caption=messages['choose_style_pic']),
                                  reply_markup=demo_style_set[number])
    async with state.proxy() as data:
        data['selected_style'] = number
        already_received = data['number_of_styles_received']
        if already_received == 0:
            if len(data['path_to_style']) == 0:
                data['path_to_style'].append(f'style_large/style_({number}).png')
            elif len(data['path_to_style']) == 1:
                data['path_to_style'][0] = f'style_large/style_({number}).png'
        if already_received == 1:
            if len(data['path_to_style']) == 1:
                data['path_to_style'].append(f'style_large/style_({number}).png')
            elif len(data['path_to_style']) == 2:
                data['path_to_style'][1] = f'style_large/style_({number}).png'


# -----------------------
# Сообщение: Стиль успешно загружен.
# Кнопка: "Далее"
# -----------------------
# Меню: Выберите стиль из коллекции.
# Кнопка: "Готово"
# -----------------------
@dp.callback_query_handler(text='accept_uploaded_img', state=NSTStates.style_imgs_accepted)
@dp.callback_query_handler(text='accept_style', state=NSTStates.quantity_accepted)
async def accept_style(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['number_of_styles_received'] += 1
        # Проверяем список ссылок на стили. Если длина списка меньше чем "собрано" стилей, значит мы не кликали
        # кнопки-варианты стиля, и нажали "Готово" с выбранным по умолчанию первым стилем. Поэтому в словарь
        # ничего не было добавлено. Добавляем ссылку на первый стиль.
        if len(data['path_to_style']) < data['number_of_styles_received']:
            data['path_to_style'].append('style_large/style_(1).png')
    selected_style_quantity = await get_from_state('selected_style_quantity', state)
    styles_received = await get_from_state('number_of_styles_received', state)
    if selected_style_quantity == str(styles_received):
        await NSTStates.style_imgs_accepted.set()
        await call.message.delete()
        if styles_received == 2:
            await call.message.answer(text=messages['ratio_select'],
                                      reply_markup=ratio_set['50_50'])
            return
        selected_resolution = await get_from_state('selected_resolution', state)
        selected_epoch = await get_from_state('selected_epoch', state)
        size = await get_from_state('wh_content_size', state)
        predicted_time = await calc_processing_time(size, int(selected_resolution), int(selected_epoch))
        await call.message.answer(text = messages['settings_menu'] + predicted_time,
                                  reply_markup = resolution_epoch_set[f'{selected_resolution}_{selected_epoch}'])
    else:
        if call.data == "accept_style":
            await call.message.edit_media(media=InputMediaPhoto(open(f'style_demos/demo_(1).png', 'rb'),
                                          caption=messages['choose_style2_pic']),
                                          reply_markup=demo_style_set[str(1)])
        elif call.data == "accept_uploaded_img":
            await NSTStates.quantity_accepted.set()
            await call.message.delete()
            await call.message.answer(text=messages['upload_style_2'])


# -----------------------
# Опция: <выбрано 2 стиля>
# Меню: Теперь выберите в какой пропорции...
# Кнопки (навигация): "10/90", "30/70", "50/50", "70/30", "90/10"
# -----------------------
@dp.callback_query_handler(select_ratio_callback.filter(action='set_ratio'), state=NSTStates.style_imgs_accepted)
async def set_ratio(call: CallbackQuery, callback_data: dict, state: FSMContext):
    ratio = callback_data.get("ratio")
    await call.message.edit_reply_markup(reply_markup=ratio_set[ratio])
    async with state.proxy() as data:
        data['selected_ratio'] = ratio


# -----------------------
# Опция: <выбрано 2 стиля>
# Меню: Теперь выберите в какой пропорции...
# Кнопка: "Принять"
# -----------------------
@dp.callback_query_handler(text='accept_ratio', state=NSTStates.style_imgs_accepted)
async def accept_ratio(call: CallbackQuery, state: FSMContext):
    selected_resolution = await get_from_state('selected_resolution', state)
    selected_epoch = await get_from_state('selected_epoch', state)
    size = await get_from_state('wh_content_size', state)
    predicted_time = await calc_processing_time(size, int(selected_resolution), int(selected_epoch))
    await call.message.edit_text(text = messages['settings_menu'] + predicted_time,
                                 reply_markup = resolution_epoch_set[f'{selected_resolution}_{selected_epoch}'])


# -----------------------
# Меню: Выберите один из режимов...
# Кнопки (навигация): "Demo", "Standart", "Maximal"
# Кнопки (навигация): "5 шагов", "10 шагов", "15 шагов"
# -----------------------
@dp.callback_query_handler(select_settings_callback.filter(), state=NSTStates.style_imgs_accepted)
async def set_settings(call: CallbackQuery, callback_data: dict, state: FSMContext):
    size = await get_from_state('wh_content_size', state)
    resolution = callback_data.get("resolution")
    epoch = callback_data.get("epoch")
    predicted_time = await calc_processing_time(size, int(resolution), int(epoch))
    await call.message.edit_text(text = messages['settings_menu'] + predicted_time,
                                 reply_markup = resolution_epoch_set[f'{resolution}_{epoch}'])
    async with state.proxy() as data:
        data['selected_resolution'] = resolution
        data['selected_epoch'] = epoch


# -----------------------
# Меню: Выберите один из режимов...
# Кнопка: "Готово"
# -----------------------
@dp.callback_query_handler(text='accept_settings', state=NSTStates.style_imgs_accepted)
async def accept_settings(call: CallbackQuery, state: FSMContext):
    await NSTStates.ready_to_transfer.set()
    msg = await get_final_message(await state.get_data())
    await call.message.edit_text(text=msg, reply_markup=run_nst_menu)


# -----------------------
# Меню: Финальное меню.
# Кнопка: "Назад к настройкам"
# -----------------------
@dp.callback_query_handler(text='back_to_settings', state=NSTStates.ready_to_transfer)
async def back_to_settings(call: CallbackQuery, state: FSMContext):
    await NSTStates.style_imgs_accepted.set()
    selected_resolution = await get_from_state('selected_resolution', state)
    selected_epoch = await get_from_state('selected_epoch', state)
    size = await get_from_state('wh_content_size', state)
    predicted_time = await calc_processing_time(size, int(selected_resolution), int(selected_epoch))
    await call.message.edit_text(text = messages['settings_menu'] + predicted_time,
                                 reply_markup = resolution_epoch_set[f'{selected_resolution}_{selected_epoch}'])


################################################################################################################

# -----------------------
# Меню: Финальное меню.
# Кнопка: "Поехали!"
# -----------------------
@dp.callback_query_handler(text='run_transfer', state=NSTStates.ready_to_transfer)
async def run_nst(call: CallbackQuery, state: FSMContext):
    vgg_directory = 'direct.pth'
    
    await call.message.delete_reply_markup()
    await call.message.answer('Стартуем', reply_markup=ReplyKeyboardRemove())
    start_time = datetime.now()

    style_layers = ['conv1_1','conv2_1','conv3_1','conv4_1','conv5_1']
    content_layers = ['conv4_2']

    style_paths = await get_styles_dict(state)
    epoch = int(await get_from_state('selected_epoch', state))
    content_path = await get_from_state('path_to_content', state)

    imsize = int(await get_from_state('selected_resolution', state))
    normalize_weights(style_paths)

    style_images = [(load_img(path, imsize), relative_weight) for path, relative_weight in style_paths.items()]
    content_image = load_img(content_path, imsize)

    nst_model = get_model(path_to_pretrained=vgg_directory, pooling='avg')
    targets = get_targets(nst_model, style_layers, content_layers, style_images, content_image)

    loss_funcs = get_loss_funcs(style_layers, content_layers)
    loss_layers = style_layers + content_layers

    style_weight = 1e3
    content_weight = 1
    factor = 1. / len(style_layers)
    weights = [style_weight * factor] * len(style_layers) + [content_weight] * len(content_layers)

    optimImg = Variable(content_image.data.clone(), requires_grad=True)
    optimizer = optim.LBFGS([optimImg])

    gc.collect()
    await NSTStates.in_process.set()
    await call.message.answer('Трансфер стиля запущен')

    img = run_style_transfer(model = nst_model,
                             optim_img = optimImg,
                             optimizer = optimizer,
                             iter_num = epoch,
                             loss_layers = loss_layers,
                             targets = targets,
                             loss_funcs = loss_funcs,
                             weights = weights)

    save_img(img)
    gc.collect()

    photo = {'photo': open('result.png', 'rb')}
    
    total_time = datetime.now() - start_time

    await call.message.answer_photo(photo=photo['photo'])
    await call.message.answer(f'Время трансфера: {total_time - timedelta(microseconds=total_time.microseconds)} \nЧтобы начать сначала введите /start')

    await state.reset_state()

################################################################################################################


#########################################################
#                         Utils                         #
#########################################################

async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text=messages['admin_notification'])


async def get_from_state(key, state):
    data = await state.get_data()
    value = data.get(key)
    return value


async def get_styles_dict(state):
    async with state.proxy() as data:
        style_list = data['path_to_style']
        style_ratio = data['selected_ratio']
    ratio_values = [int(val) for val in style_ratio.split("_")]
    result = {}
    # if len(style_list) > 1:
    #     for i in range(len(style_list)):
    #         result[style_list[i]] = ratio_values[i]
    for i in range(len(style_list)):
        result[style_list[i]] = ratio_values[i]
    return result


async def get_image_size(filepath):
    with Image.open(filepath) as img:
        size = img.size
    return size


async def calc_processing_time(size, resolution, epoch):
    # 0.000557 коэффициент рассчитан на основе данных экспериментальных запусков (Intel Skylake CPU),
    # равен среднему времени обсчёта одного пикселя в одной эпохе (в секундах).
    w, h = size
    dim_1 = resolution
    dim_2 = round((max(w, h) / min(w, h)) * resolution)
    seconds = dim_1 * dim_2 * epoch * 0.000557
    return str(timedelta(seconds=round(seconds)))

async def get_final_message(state_data):
    source = "Выбранная" if (state_data['selected_content_source'] == 'collection') else "Загруженная"
    procedure = "уменьшена" if (min(state_data['wh_content_size']) > int(state_data['selected_resolution'])) else "увеличена"
    new_size = state_data['selected_resolution']
    steps = state_data['selected_epoch']
    transfer = "перенесён 1 новый стиль" if (state_data['selected_style_quantity'] == '1') else "перенесено 2 новых стиля в соотношении "
    ratio = "" if (state_data['selected_style_quantity'] == '1') else state_data['selected_ratio'][:2] + '/' + state_data['selected_ratio'][3:]

    message = f"{source} контент-картинка будет пропорционально {procedure} до {new_size} пикселей по меньшей стороне, после чего за {steps} шагов на неё \
будет {transfer}{ratio}.\n\nЕсли всё верно - жми «Поехали!»"
    return message
