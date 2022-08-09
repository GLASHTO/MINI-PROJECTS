from aiogram import Bot ,types 
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove 
import string, json, re ,random
 
   
#текста и данные 
text_for_start = 'Это главный асинхронный(пока на async/await(какой же я лошара)) Бот-отец ,который будет с младшими ботами ,пока не знаю как и даже не представляю чего хочу но будет интересно .Будем работать в эту ночь чтоб ваши нецензурные слова дамы и господа были удалены из этого чата'

text_for_error = 'Общение с ботом в ЛС:\n@Frdjbot\nhttp://t.me/Frdjbot'

about_bot = 'Этот Бот будет уметь очищать маты;\nОтправлять фотки и видео по  id;\nПредоставлять достум к моим сайтам ,а также делиться ссылками на них;\nБудут добалвены шахматы(устные)' 

key_del = 'Чтобы вызывать клавиатуру отправьте /start'

text_for_OTK = 'вызов скрывающейся клавиатуры'

arr_with_mats = json.load(open('damn.json'))
TOKEN = '2001852541:AAGNXaOYmaoyBDZDhj3JDZc74zsRooqIGvc'
#бот принимающиц значение токена 
bot = Bot(token=TOKEN)
#обработчик действий пользователя 
dp=Dispatcher(bot)
#то что происходит перед стартом бота  
def on_startup():
	print('Холо проснулась ,услужи ей)')
#@dp.message_handler()
#async def echo_bot(msg : types.Message):
	#отвечает на сообщение с упоминанием в том же чате (либо в общую гр ,либо в лс)
	#await msg.reply(msg.text )
	#ответ без упоминания после запуска ,также как и reply в тот же чат в котором написали
	#await msg.answer(msg.text)
	#send_message действие конкретно бота и он будучи запущенным пользователем отправляет сообщение в личку
	#if msg.text.lower() == 'ю':	
#		await bot.send_message(msg.from_user.id ,'похую')
#клавиатура
number = KeyboardButton('send number', request_contact = True)
geo = KeyboardButton('send location', request_location = True)

start = KeyboardButton('/start')
possiblity = KeyboardButton('/possiblity')
one_time_keyboard_button = KeyboardButton('/one_time_keyboard')
delete = KeyboardButton('/delete_keyboard')

start_keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
start_keyboard.row(possiblity, one_time_keyboard_button).row(number, geo).row(delete, start)
#одноразовая клавиатура
hide_keyboard = KeyboardButton('hide')
back_to_normalkey = KeyboardButton('/back')
one_time_keyboard_ = ReplyKeyboardMarkup(resize_keyboard = True,one_time_keyboard = True)
one_time_keyboard_.row(hide_keyboard, back_to_normalkey)
#команды и сообщения 
@dp.message_handler(commands = ['help','start'])
async def bot_start(msg:types.Message):
		try:	
			await bot.send_message(msg.from_user.id, text_for_start, reply_markup = start_keyboard)
			#то сообщение на которое отреагировала эта часть кода - будет удалена
			await msg.delete()
		except:
			#async def bot_send_msg_for_the_user_error():
			await msg.reply(text_for_error)
			await msg.delete()
	
@dp.message_handler(commands = ['possiblity'])
async def bot_possibility(msg:types.Message):
		await msg.reply(about_bot)
		
		
@dp.message_handler(commands = ['delete_keyboard'])
async def delete_keyboard(msg : types.Message):
	await msg.answer(key_del,reply_markup = ReplyKeyboardRemove())
	


@dp.message_handler(commands = ['one_time_keyboard'])
async def one_time_keyboard(msg : types.Message):
	await bot.send_message(msg.from_user.id,text_for_OTK, reply_markup = one_time_keyboard_)
@dp.message_handler(commands = ['back'])
async def back_to(msg : types.Message):
	await msg.answer('Ok',reply_markup = start_keyboard)
	
	
#пустой хэндлер всегда внизу, иначе он будет перехватывать сообщения и команды не будут исполняться 
@dp.message_handler()
async def mats(msg : types.Message):
	if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in msg.text.split(' ')}.intersection(set(arr_with_mats)) != set():
		await msg.reply('Попалась шл@шка')
		await msg.delete()

# 🥲
#===усовершенствовать фильтр матов===
#--
#массив со сбором найденных слов-смысл? 
	#len_intersection = []
#--
	
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

#--
#		if search_word is not None:
#			len_intersection.append(search_word)
#--

#--	
#		print(len_intersection)
#		
#	if len_intersection is not None:
#		await msg.reply('Попалась шлюх@')
#		await msg.delete()
#--
#======	
		



#два вида запуска ,"long polling" постоянно обращается к серверу с желанием узнать не пришло ли сообщение и "webhook" бот 'спит' до того момента пока не придет сообщение от сервера тг 
executor.start_polling(dp ,skip_updates = True ,on_startup= on_startup())