from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from aiogram import Dispatcher
from aiogram import types

# Инлайн клавиатура
inline_markup_properties = InlineKeyboardMarkup(row_width=2)
get_push = InlineKeyboardButton(text='get_push', callback_data='push')
get_push_msg = InlineKeyboardButton(text='push_msg', callback_data= 'push_msg')
get_push_alert = InlineKeyboardButton(text='push_alert', callback_data= 'push_alert')
get_url = InlineKeyboardButton(text='url_youtube', url='https://www.youtube.com/')


# callback but that notification
# @dp.callback_query_handler(text='push')
async def push(cbk: types.CallbackQuery):
    await cbk.answer('poshel v jopu izvrashenec')


#callback but that message
# @dp.callback_query_handler(text='push_msg')
async def push_message(cbk: types.CallbackQuery):
    await cbk.message.answer('ty odinok')
    # для того чтобы убрать знак загрузки
    await cbk.answer()


#callback but that alert, помещает в себя до 200 значений
# @dp.callback_query_handler(text='push_alert')
async def alert(cbk: types.CallbackQuery):
    await cbk.answer('this alert',show_alert=True)

# также можно группировать кнопки
# test = [InlineKeyboardButton(text='get_push',callback_data='https://www.youtube.com/' ),InlineKeyboardButton(text='url_youtube',url='https://www.youtube.com/')]
# insert - добавляет кнопкку в ту же строку
# add - устанавливает автоматом, на строку столько кнопок, сколько задано в параметре InlineMarkupKeyboard
# row - столько кнопок на строку сколько задано. Если их слишком много происходит перенос на след строку

inline_markup_properties.add(get_push, get_url).row(get_push_msg,get_push_alert)  # .add(*test)


def register_inline_kb_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(push,text='push')
    dp.register_callback_query_handler(push_message,text='push_msg')
    dp.register_callback_query_handler(alert,text='push_alert')
