from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#ЛС
class FSMNFC(StatesGroup):
    name = State()  # 'get name for the NFC'
    photo = State()  # 'photo for the NFC'
    description = State()  # 'about this NFC'


# start = 'get user agree on the start create a NFC'
@dp.message_handler(lambda msg: msg.text.lower() == "pls_new_nfc",
                    state=None)  # если делать поиск по слову (литерал is ,не рабоает)
# @dp.message_handler(lambda msg: msg in "все что угодно(переменная и т.д.)", state=None)
async def start(msg: types.Message):
    await FSMNFC.name.set()
    await bot.send_message(msg.from_user.id, "Give name to your NFC")


#
@dp.message_handler(commands=['exit'], state="*")
@dp.message_handler(Text(equals='exit', ignore_case=True), state="*")
async def cancel(msg: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer('Ok, Sir')


@dp.message_handler(state=FSMNFC.name)
async def name_of_the_nfc(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await FSMNFC.next()
    await msg.reply('send the photo for the NFC')


arr_with_photo = []


@dp.message_handler(content_types=['photo'], state=FSMNFC.photo)
async def photo_for_the_nfc(msg: types.Message, state: FSMContext):
    await msg.answer('for end ,click DONE ')
    # разобраться в базах данных ,чтобы уметь ложить массивы в таблицу
    async with state.proxy() as data:
        data['photo'] = msg.photo[0].file_id
        # data= {'name':msg.photo}


@dp.message_handler(Text(equals='DONE'), state=FSMNFC.photo)
async def photo_done(msg: types.Message):
    await FSMNFC.next()
    await msg.reply('description:')


@dp.message_handler(state=FSMNFC.description)
async def description(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = msg.text
    await msg.reply("LOAD...")
    cur_nfc.execute('''INSERT INTO nfc_info VALUES (?,?,?)
    ''', tuple(data.values()))
    db_nfc.commit()
    await state.finish()


class For_vid(StatesGroup):
    vid = State()  # load the vid ID


@dp.message_handler(lambda msg: msg.text.lower() == "load_the_video", state=None)
async def load_video(msg: types.Message):
    await For_vid.vid.set()
    await bot.send_message(msg.from_user.id, 'send the video')


@dp.message_handler(content_types=['video'], state=For_vid.vid)
async def get_the_videos(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['video'] = msg.video.file_id
        cur_vid.execute('''INSERT INTO video_id VALUES(?)''', tuple(data.values()))
        db_vid.commit()
        await bot.send_message(msg.from_user.id, f'video loaded, ID:\n{data["video"]}')


@dp.message_handler(lambda msg: msg.text == "DONE", state=For_vid.vid)
async def finish_loading(msg: types.Message, state: FSMContext):
    await msg.answer('all videos loaded')
    await state.finish()