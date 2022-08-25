# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher, FSMContext
# from aiogram.utils import executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher.filters import Text
# import string
# import json
# import sqlite3  # , re ,random

# storage = MemoryStorage()
# db_nfc = sqlite3.connect('nfc.db')
# db_admin = sqlite3.connect('admin.db')
# db_vid = sqlite3.connect('video.db')
#
# cur_nfc = db_nfc.cursor()
# cur_admin = db_admin.cursor()
# cur_vid = db_vid.cursor()
# текста и данные
# text_for_start = 'Это главный асинхронный(пока на async/await(какой же я лошара)) Бот-отец ,который будет с ' \
#                  'младшими ботами ,пока не знаю как и даже не представляю чего хочу но будет интересно .Будем ' \
#                  'работать в эту ночь чтоб ваши нецензурные слова дамы и господа были удалены из этого чата'
#
# text_for_error = 'Общение с ботом в ЛС:\n@Frdjbot\nhttp://t.me/Frdjbot'
#
# about_bot = 'Этот Бот будет уметь очищать маты;\nОтправлять фотки и видео по  id;\nПредоставлять достум к моим ' \
#             'сайтам ,а также делиться ссылками на них;\nБудут добалвены шахматы(устные)'
#
# key_del = 'Чтобы вызывать клавиатуру отправьте /start'
#
# text_for_OTK = 'вызов скрывающейся клавиатуры'

# arr_with_mats = json.load(
#     open(r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\pytelebot\Bot_father\pycache\damn.json'))
# TOKEN = '2001852541:AAGNXaOYmaoyBDZDhj3JDZc74zsRooqIGvc'
# # бот принимающиц значение токена
# bot = Bot(token=TOKEN)
# # обработчик действий пользователя
# dp = Dispatcher(bot, storage=storage)


# async def get_data(msg, db, table):
#     for data in db.execute(f'SELECT * FROM {table}').fetchall():
#         await bot.send_message(msg.from_user.id, data[0])


# то что происходит перед стартом бота
# def on_startup():
#     cur_vid.execute('''CREATE TABLE IF NOT EXISTS video_id(
#     video TEXT
#     )
#     ''')
#     cur_admin.execute('''CREATE TABLE IF NOT EXISTS admin_info(
#     trial_write VARCHAR)
#     ''')
#     cur_nfc.execute('''CREATE TABLE IF NOT EXISTS nfc_info(
#     name VARCHAR,
#     photo TEXT,
#     description TEXT
#     )''')
#     db_admin.commit()
#     db_vid.commit()
#     db_nfc.commit()
#     print('Холо проснулась ,услужи ей)')


# @dp.message_handler()
# async def echo_bot(msg : types.Message):
# отвечает на сообщение с упоминанием в том же чате (либо в общую гр ,либо в лс)
# await msg.reply(msg.text )
# ответ без упоминания после запуска ,также как и reply в тот же чат в котором написали
# await msg.answer(msg.text)
# send_message действие конкретно бота и он будучи запущенным пользователем отправляет сообщение в личку
# if msg.text.lower() == 'ю':
#		await bot.send_message(msg.from_user.id ,'похую')
# # Инлайн клавиатура
# inline_markup_properties = InlineKeyboardMarkup(row_width=2)
# get_push = InlineKeyboardButton(text='get_push', callback_data='push')
# get_push_msg = InlineKeyboardButton(text='push_msg', callback_data= 'push_msg')
# get_push_alert = InlineKeyboardButton(text='push_alert', callback_data= 'push_alert')
# get_url = InlineKeyboardButton(text='url_youtube', url='https://www.youtube.com/')
#
#
# # callback but that notification
# @dp.callback_query_handler(text='push')
# async def push(cbk: types.CallbackQuery):
#     await cbk.answer('poshel v jopu izvrashenec')
#
#
# #callback but that message
# @dp.callback_query_handler(text='push_msg')
# async def push_message(cbk: types.CallbackQuery):
#     await cbk.message.answer('ty odinok')
#     # для того чтобы убрать знак загрузки
#     await cbk.answer()
#
#
# #callback but that alert, помещает в себя до 200 значений
# @dp.callback_query_handler(text='push_alert')
# async def alert(cbk: types.CallbackQuery):
#     await cbk.answer('this alert',show_alert=True)
#
# # также можно группировать кнопки
# # test = [InlineKeyboardButton(text='get_push',callback_data='https://www.youtube.com/' ),InlineKeyboardButton(text='url_youtube',url='https://www.youtube.com/')]
# # insert - добавляет кнопкку в ту же строку
# # add - устанавливает автоматом, на строку столько кнопок, сколько задано в параметре InlineMarkupKeyboard
# # row - столько кнопок на строку сколько задано. Если их слишком много происходит перенос на след строку
# inline_markup_properties.add(get_push, get_url).row(get_push_msg,get_push_alert)  # .add(*test)
# # клавиатура
# number = KeyboardButton('send number', request_contact=True)
# geo = KeyboardButton('send location', request_location=True)
#
# start = KeyboardButton('/start')
# possibility = KeyboardButton('possibility')
# one_time_keyboard_button = KeyboardButton('one_time_keyboard')
# delete = KeyboardButton('delete_keyboard')
#
# # вызов инлайн клавиатуры
# inline_keyboard = KeyboardButton(text='inline_kb')
#
# start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# start_keyboard.add(possibility).row( one_time_keyboard_button, inline_keyboard).row(number, geo).row(delete, start)
# # одноразовая клавиатура
# hide_keyboard = KeyboardButton('hide')
# back_to_normalkey = KeyboardButton('back')
# one_time_keyboard_ = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# one_time_keyboard_.row(hide_keyboard, back_to_normalkey)
#

# команды и сообщения
# # общий
# @dp.message_handler(commands=['help', 'start'])
# async def bot_start(msg: types.Message):
#     try:
#         await bot.send_message(msg.from_user.id, text_for_start, reply_markup=start_keyboard)
#         # то сообщение на которое отреагировала эта часть кода - будет удалена
#         await msg.delete()
#     except:
#         # async def bot_send_msg_for_the_user_error():
#         await msg.reply(text_for_error)
#         await msg.delete()


# #ЛС
# class FSMNFC(StatesGroup):
#     name = State()  # 'get name for the NFC'
#     photo = State()  # 'photo for the NFC'
#     description = State()  # 'about this NFC'
#
#
# # start = 'get user agree on the start create a NFC'
# @dp.message_handler(lambda msg: msg.text.lower() == "pls_new_nfc",
#                     state=None)  # если делать поиск по слову (литерал is ,не рабоает)
# # @dp.message_handler(lambda msg: msg in "все что угодно(переменная и т.д.)", state=None)
# async def start(msg: types.Message):
#     await FSMNFC.name.set()
#     await bot.send_message(msg.from_user.id, "Give name to your NFC")
#
#
# #
# @dp.message_handler(commands=['exit'], state="*")
# @dp.message_handler(Text(equals='exit', ignore_case=True), state="*")
# async def cancel(msg: types.Message, state: FSMContext):
#     current_state = state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await msg.answer('Ok, Sir')
#
#
# @dp.message_handler(state=FSMNFC.name)
# async def name_of_the_nfc(msg: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = msg.text
#     await FSMNFC.next()
#     await msg.reply('send the photo for the NFC')
#
#
# arr_with_photo = []
#
#
# @dp.message_handler(content_types=['photo'], state=FSMNFC.photo)
# async def photo_for_the_nfc(msg: types.Message, state: FSMContext):
#     await msg.answer('for end ,click DONE ')
#     # разобраться в базах данных ,чтобы уметь ложить массивы в таблицу
#     async with state.proxy() as data:
#         data['photo'] = msg.photo[0].file_id
#         # data= {'name':msg.photo}
#
#
# @dp.message_handler(Text(equals='DONE'), state=FSMNFC.photo)
# async def photo_done(msg: types.Message):
#     await FSMNFC.next()
#     await msg.reply('description:')
#
#
# @dp.message_handler(state=FSMNFC.description)
# async def description(msg: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['description'] = msg.text
#     await msg.reply("LOAD...")
#     cur_nfc.execute('''INSERT INTO nfc_info VALUES (?,?,?)
#     ''', tuple(data.values()))
#     db_nfc.commit()
#     await state.finish()
#
#
# class For_vid(StatesGroup):
#     vid = State()  # load the vid ID
#
#
# @dp.message_handler(lambda msg: msg.text.lower() == "load_the_video", state=None)
# async def load_video(msg: types.Message):
#     await For_vid.vid.set()
#     await bot.send_message(msg.from_user.id, 'send the video')
#
#
# @dp.message_handler(content_types=['video'], state=For_vid.vid)
# async def get_the_videos(msg: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['video'] = msg.video.file_id
#         cur_vid.execute('''INSERT INTO video_id VALUES(?)''', tuple(data.values()))
#         db_vid.commit()
#         await bot.send_message(msg.from_user.id, f'video loaded, ID:\n{data["video"]}')
#
#
# @dp.message_handler(lambda msg: msg.text == "DONE", state=For_vid.vid)
# async def finish_loading(msg: types.Message, state: FSMContext):
#     await msg.answer('all videos loaded')
#     await state.finish()


# @dp.message_handler(Text(equals='nfc_info', ignore_case=True))
# async def get_nfc_info(msg: types.Message):
#     await get_data(msg=msg, db=db_nfc, table='nfc_info')
#
#
# @dp.message_handler(Text(equals='admin_info', ignore_case=True))
# async def get_nfc_info(msg: types.Message):
#     await get_data(msg=msg, db=db_admin, table='admin_info')
#
#
# @dp.message_handler(Text(equals='vid_id', ignore_case=True))
# async def get_nfc_info(msg: types.Message):
#     for data in db_vid.execute(f'SELECT * FROM video_id').fetchall():
#         await bot.send_video(msg.from_user.id, data[0])


# Админ
# admin_id = None
#
#
# class FSMNAdmin(StatesGroup):
#     trial_write = State()  # пробная админка
#
#
# # как пример проверки является ли пользователь админом,  метод  is_chat_admin при передаче true ,
# # проверяет являтся ли пользователь написавший команду - админом
# # важное дополнение - проверка работает только если сообщение отправлено в чат
# @dp.message_handler(lambda msg: msg.text.lower() == 'admin_try', is_chat_admin=True, state=None)
# async def trial_write_admin(msg: types.Message, state: FSMContext):
#     global admin_id
#     await bot.send_message(msg.from_user.id, 'yes_sir?')
#     await msg.delete()
#     admin_id = msg.from_user.id
#     if msg.from_user.id == admin_id:
#         await FSMNAdmin.trial_write.set()
#
#
# @dp.message_handler(state=FSMNAdmin.trial_write)
# async def try_ad(msg: types.Message, state: FSMContext):
#     if msg.from_user.id == admin_id:
#         async with state.proxy() as data:
#             data['admin_id'] = admin_id
#         cur_admin.execute('''INSERT INTO admin_info VALUES(?)''', tuple(data.values()))
#         db_admin.commit()
#
#
# @dp.message_handler()
# async def ad_try_end(msg: types.Message, state: FSMContext):
#     if msg.from_user.id == admin_id:
#         await state.finish()
#         await bot.send_message(msg.from_user.id, f'Admin ID:\n{admin_id}')


# # пустой хэндлер всегда внизу, иначе он будет перехватывать сообщения и команды не будут исполняться
# @dp.message_handler()
# async def mats(msg: types.Message):
#     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in msg.text.split(' ')}.intersection(
#             set(arr_with_mats)) != set():
#         await msg.reply('Попалась шл@шка')
#         await msg.delete()


# 🥲
# ===усовершенствовать фильтр матов===
# --
# массив со сбором найденных слов-смысл?
# len_intersection = []
# --

#	text = msg.text.lower().split(' ')
#	print(text)
#	for mats in arr_with_mats:
#		print(mats)


#		--len_intersection.append(''.join(re.findall(str({word.lower().strip().translate(str.maketrans('','',string.punctuation)) for word in text})+r'?',mats)))
#	print(str({word.lower().strip().translate(str.maketrans('','',string.punctuation)) for word in text}),str({mats for mats in arr_with_mats}))

#	search_word = re.search(str({word.lower().strip().translate(str.maketrans('','',string.punctuation)) for word in text}),str(''.join({mats for mats in arr_with_mats})))

#	mats=''.join(arr_with_mats)
#	print (mats)
#	for word in text:
#		search_word = re.search(r'\B'+word.lower().strip().translate(str.maketrans('','',string.punctuation))+r'\B',mats)

#	print(search_word)
#	if search_word is not None:
#		await msg.reply('Попалась шлюх@')
#		await msg.delete()

# --
#		if search_word is not None:
#			len_intersection.append(search_word)
# --

# --
#		print(len_intersection)
#		
#	if len_intersection is not None:
#		await msg.reply('Попалась шлюх@')
#		await msg.delete()
# --
# ======


# два вида запуска ,"long polling" постоянно обращается к серверу с желанием узнать не пришло ли сообщение и "webhook" бот 'спит' до того момента пока не придет сообщение от сервера тг
# executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
