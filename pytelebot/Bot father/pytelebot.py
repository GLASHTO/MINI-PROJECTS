from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = MemoryStorage()

import string, json  # , re ,random
import sqlite3

# текста и данные
text_for_start = 'Это главный асинхронный(пока на async/await(какой же я лошара)) Бот-отец ,который будет с младшими ботами ,пока не знаю как и даже не представляю чего хочу но будет интересно .Будем работать в эту ночь чтоб ваши нецензурные слова дамы и господа были удалены из этого чата'

text_for_error = 'Общение с ботом в ЛС:\n@Frdjbot\nhttp://t.me/Frdjbot'

about_bot = 'Этот Бот будет уметь очищать маты;\nОтправлять фотки и видео по  id;\nПредоставлять достум к моим сайтам ,а также делиться ссылками на них;\nБудут добалвены шахматы(устные)'

key_del = 'Чтобы вызывать клавиатуру отправьте /start'

text_for_OTK = 'вызов скрывающейся клавиатуры'

arr_with_mats = json.load(open('damn.json'))
TOKEN = '2001852541:AAGNXaOYmaoyBDZDhj3JDZc74zsRooqIGvc'
# бот принимающиц значение токена
bot = Bot(token=TOKEN)
# обработчик действий пользователя
dp = Dispatcher(bot, storage=storage)


# то что происходит перед стартом бота
def on_startup():
    print('Холо проснулась ,услужи ей)')


# @dp.message_handler()
# async def echo_bot(msg : types.Message):
# отвечает на сообщение с упоминанием в том же чате (либо в общую гр ,либо в лс)
# await msg.reply(msg.text )
# ответ без упоминания после запуска ,также как и reply в тот же чат в котором написали
# await msg.answer(msg.text)
# send_message действие конкретно бота и он будучи запущенным пользователем отправляет сообщение в личку
# if msg.text.lower() == 'ю':
#		await bot.send_message(msg.from_user.id ,'похую')
# клавиатура
number = KeyboardButton('send number', request_contact=True)
geo = KeyboardButton('send location', request_location=True)

start = KeyboardButton('/start')
possiblity = KeyboardButton('/possiblity')
one_time_keyboard_button = KeyboardButton('/one_time_keyboard')
delete = KeyboardButton('/delete_keyboard')

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.row(possiblity, one_time_keyboard_button).row(number, geo).row(delete, start)
# одноразовая клавиатура
hide_keyboard = KeyboardButton('hide')
back_to_normalkey = KeyboardButton('/back')
one_time_keyboard_ = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
one_time_keyboard_.row(hide_keyboard, back_to_normalkey)


# команды и сообщения
# общий
@dp.message_handler(commands=['help', 'start'])
async def bot_start(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, text_for_start, reply_markup=start_keyboard)
        # то сообщение на которое отреагировала эта часть кода - будет удалена
        await msg.delete()
    except:
        # async def bot_send_msg_for_the_user_error():
        await msg.reply(text_for_error)
        await msg.delete()


# ЛС
@dp.message_handler(commands=['possiblity'])
async def bot_possibility(msg: types.Message):
    await bot.send_message(msg.from_user.id, about_bot)


@dp.message_handler(commands=['delete_keyboard'])
async def delete_keyboard(msg: types.Message):
    await bot.send_message(msg.from_user.id, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['one_time_keyboard'])
async def one_time_keyboard(msg: types.Message):
    await bot.send_message(msg.from_user.id, text_for_OTK, reply_markup=one_time_keyboard_)


@dp.message_handler(commands=['back'])
async def back_to(msg: types.Message):
    await bot.send_message(msg.from_user.id, reply_markup=start_keyboard)

class FSMNFC(StatesGroup):
    name = State()  # 'get name for the NFC'
    photo = State()  # 'photo for the NFC'
    description = State()  # 'about this NFC'


# start = 'get user agree on the start create a NFC'
@dp.message_handler(lambda msg: msg.text.lower() == "pls_new_nfc",
                    state=None)  # если делать поиск по слову (литерал is ,не рабоает) @dp.message_handler(lambda msg: msg in "все что угодно(переменная и т.д.)", state=None)
async def start(msg: types.Message):
    await FSMNFC.name.set()
    await bot.send_message(msg.from_user.id, "Give name to your NFC")


@dp.message_handler(state=FSMNFC.name)
async def name_of_the_NFC(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await FSMNFC.next()
    await msg.reply('send the photo for the NFC')


@dp.message_handler(content_types=['photo'], state=FSMNFC.photo)
async def photo_for_the_NFC(msg: types.Message, state: FSMContext):
    await msg.answer('for end ,click DONE ')
    async with state.proxy() as data:
        data['photo'] = [].append(msg.photo[0].file_id)
        # data= {'name':msg.photo}
    if msg.text == 'DONE':
        await FSMNFC.next()
        await msg.reply('description:')


@dp.message_handler(state=FSMNFC.description)
async def description(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = msg.text
    await msg.reply("LOAD...")
    await state.finish()


class for_vid(StatesGroup):
    vid = State()  # load the vid ID


@dp.message_handler(lambda msg: msg.text.lower() == "load_the_video", state=None)
async def load_video(msg: types.Message):
    await for_vid.vid.set()
    await bot.send_message(msg.from_user.id, 'send the video')


@dp.message_handler(content_types=['video'], state=for_vid.vid)
async def get_the_videos(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['video'] = msg.video.file_id
        await bot.send_message(msg.from_user.id, f'video loaded, ID:\n{data["video"]}')


@dp.message_handler(lambda msg: msg.text == "DONE")
async def finish_loading(msg: types.Message, state=FSMContext):
    await state.finish()
    await bot.send_message(msg.from_user.id, 'all videos loaded')


# Админ
admin_id = None
class FSMNAdmin(StatesGroup):
    trial_write = State()  # пробная админка
#как пример проверки является ли пользователь админом,  метод  is_chat_admin при передаче true ,проверяет являтся ли пользователь написавший команду - админом
@dp.message_handler(lambda msg: msg.text.lower() == 'admin_try', is_chat_admin = True, state=FSMNAdmin.trial_write)
async def trial_write_admin(msg: types.Message, state: FSMContext):
    global admin_id
    await bot.send_message(msg.from_user.id, 'yes_sir?')
    admin_id = msg.from_user.id
    if msg.from_user.id == admin_id:
        async with state.proxy() as data:
            data['admin_id'] = msg.from_user.id
        await bot.send_message(msg.from_user.id, f'Admin ID:\n{admin_id}')
        await state.finish()


# пустой хэндлер всегда внизу, иначе он будет перехватывать сообщения и команды не будут исполняться
@dp.message_handler()
async def mats(msg: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in msg.text.split(' ')}.intersection(
            set(arr_with_mats)) != set():
        await msg.reply('Попалась шл@шка')
        await msg.delete()


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
executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
