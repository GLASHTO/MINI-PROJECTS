from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from .. import bot
from .. import db_nfc, cur_nfc
from keyboards.user_keyboard.nfc_kb import nfc_kb_stop
from keyboards.user_keyboard.user_kb import start_keyboard
# ЛС
class FSMNFC(StatesGroup):
    name = State()  # 'get name for the NFC'
    photo = State()  # 'photo for the NFC'
    description = State()  # 'about this NFC'


# start = 'get user agree on the start create a NFC'
# @dp.message_handler(lambda msg: msg.text.lower() == "pls_new_nfc",
#                     state=None)  # если делать поиск по слову (литерал is ,не рабоает)
# @dp.message_handler(lambda msg: msg in "все что угодно(переменная и т.д.)", state=None)
async def start(msg: types.Message):
    await FSMNFC.name.set()
    await bot.send_message(msg.from_user.id, "Give name to your NFC",reply_markup=nfc_kb_stop)


#
# @dp.message_handler(commands=['exit'], state="*")
# @dp.message_handler(Text(equals='exit', ignore_case=True), state="*")
async def cancel(msg: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer('Ok, Sir',reply_markup=start_keyboard)


# @dp.message_handler(state=FSMNFC.name)
async def name_of_the_nfc(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await FSMNFC.next()
    await msg.reply('send the photo for the NFC')


arr_with_photo = []


# @dp.message_handler(content_types=['photo'], state=FSMNFC.photo)
async def photo_for_the_nfc(msg: types.Message, state: FSMContext):
    await msg.answer('for end ,write DONE')
    # разобраться в базах данных ,чтобы уметь ложить массивы в таблицу
    async with state.proxy() as data:
        data['photo'] = msg.photo[0].file_id
        # data= {'name':msg.photo}


# @dp.message_handler(Text(equals='DONE'), state=FSMNFC.photo)
async def photo_done(msg: types.Message):
    await msg.answer('OK',reply_markup=nfc_kb_stop)
    await FSMNFC.next()
    await msg.reply('description:')


# @dp.message_handler(state=FSMNFC.description)
async def description(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = msg.text
    cur_nfc.execute('''INSERT INTO nfc_info VALUES (?,?,?)
    ''', tuple(data.values()))
    db_nfc.commit()
    await state.finish()
    await msg.reply("LOAD...",reply_markup=start_keyboard)


def register_nfc_handlers(dp: Dispatcher):
    dp.register_message_handler(start, lambda msg: msg.text.lower() == "pls_new_nfc",
                                state=None)
    dp.register_message_handler(cancel, Text(equals='exit', ignore_case=True), state="*")
    dp.register_message_handler(name_of_the_nfc, state=FSMNFC.name)
    dp.register_message_handler(photo_for_the_nfc, content_types=['photo'], state=FSMNFC.photo)
    dp.register_message_handler(photo_done, Text(equals='DONE'), state=FSMNFC.photo)
    dp.register_message_handler(description, state=FSMNFC.description)
