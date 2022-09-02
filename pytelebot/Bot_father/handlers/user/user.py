from aiogram import types, Dispatcher
# from ..import bot
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from .. import *

# from ..keyboards.user_keyboard.user_kb import one_time_keyboard_, start_keyboard
# from ..keyboards.inline_keyboard.inline_kb import inline_markup_properties

about_bot = 'Этот Бот будет уметь очищать маты;\nОтправлять фотки и видео по  id;\nПредоставлять достум к моим ' \
            'сайтам ,а также делиться ссылками на них;\nБудут добалвены шахматы(устные)'

key_del = 'Чтобы вызывать клавиатуру отправьте /start'

text_for_OTK = 'вызов скрывающейся клавиатуры'


# ЛС
# @dp.message_handler(Text(equals='possibility'))
async def bot_possibility(msg: types.Message):
    await bot.send_message(msg.from_user.id, about_bot)


# @dp.message_handler(Text(equals='delete_keyboard'))
async def delete_keyboard(msg: types.Message):
    await bot.send_message(msg.from_user.id, key_del, reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(lambda msg: msg.text == 'one_time_keyboard')
async def one_time_keyboard(msg: types.Message):
    await bot.send_message(msg.from_user.id, text_for_OTK, reply_markup=one_time_keyboard_)


# @dp.message_handler(lambda msg: msg.text == 'back')
async def back_to(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'back to normal key', reply_markup=start_keyboard)


# @dp.message_handler(Text(equals='inline_kb'))
async def inline_kb_start(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'start inline keyboard', reply_markup=inline_markup_properties)


# @dp.message_handler(Text(equals='nfc_info', ignore_case=True))
async def get_nfc_info(msg: types.Message):
    await get_data(msg=msg, db=db_nfc, table='nfc_info')


# @dp.message_handler(Text(equals='admin_info', ignore_case=True))
async def get_admin_info(msg: types.Message):
    await get_data(msg=msg, db=db_admin, table='admin_info')


# @dp.message_handler(Text(equals='vid_id', ignore_case=True))
async def get_vid_info(msg: types.Message):
    for data in db_vid.execute(f'SELECT * FROM video_id').fetchall():
        await bot.send_video(msg.from_user.id, data[0])


# общий чат и лс
# @dp.message_handler(lambda msg: msg.text.lower().startswith('такси'))
async def tax_price(msg: types.Message):
    try:
        await msg.answer(msg.text[6:])
    except:
        await msg.reply('напишите через пробел то ,что желаете получить обратно')

async def admin_info_for_start(msg:types.Message):
    await msg.reply('Отправьте сообщение "  admin_try" в Test group:\nhttps://t.me/+RrW2DpjVbGk0ZmNi')

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(bot_possibility, Text(equals='possibility'))
    dp.register_message_handler(delete_keyboard, Text(equals='delete_keyboard'))
    dp.register_message_handler(one_time_keyboard, lambda msg: msg.text == 'one_time_keyboard')
    dp.register_message_handler(back_to, lambda msg: msg.text == 'back')
    dp.register_message_handler(inline_kb_start, Text(equals='inline_kb'))
    dp.register_message_handler(get_nfc_info, Text(equals='nfc_info', ignore_case=True))
    dp.register_message_handler(get_admin_info, Text(equals='admin_info', ignore_case=True))
    dp.register_message_handler(get_vid_info, Text(equals='vid_id', ignore_case=True))
    dp.register_message_handler(tax_price, lambda msg: msg.text.lower().startswith('такси'))
    dp.register_message_handler(admin_info_for_start, lambda msg:msg.text == 'admin_try1')
