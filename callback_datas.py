from aiogram.utils.callback_data import CallbackData

select_ratio_callback = CallbackData('post', 'action', 'ratio')
select_demo_callback = CallbackData('select', 'type', 'number')
select_quantity_callback = CallbackData('select', 'quantity')
select_operation_callback = CallbackData('select', 'type')
select_settings_callback = CallbackData('select', 'resolution', 'epoch')
select_img_source_callback = CallbackData('select', 'source')
