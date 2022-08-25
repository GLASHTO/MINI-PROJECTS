from create_bot import bot,dp
from aiogram import types,Dispatcher
from user_kb import start_keyboard
import json
import string
#текста и данные
text_for_start = 'Это главный асинхронный(пока на async/await(какой же я лошара)) Бот-отец ,который будет с ' \
                 'младшими ботами ,пока не знаю как и даже не представляю чего хочу но будет интересно .Будем ' \
                 'работать в эту ночь чтоб ваши нецензурные слова дамы и господа были удалены из этого чата'

text_for_error = 'Общение с ботом в ЛС:\n@Frdjbot\nhttp://t.me/Frdjbot'
arr_with_mats = json.load(
    open(r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\pytelebot\Bot_father\pycache\damn.json'))
# общий
# @dp.message_handler(commands=['help', 'start'])
async def bot_start(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, text_for_start, reply_markup=start_keyboard)
        # то сообщение на которое отреагировала эта часть кода - будет удалена
        await msg.delete()
    except:
        # async def bot_send_msg_for_the_user_error():
        await msg.reply(text_for_error)
        await msg.delete()
# пустой хэндлер всегда внизу, иначе он будет перехватывать сообщения и команды не будут исполняться
# @dp.message_handler()
async def mats(msg: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in msg.text.split(' ')}.intersection(
            set(arr_with_mats)) != set():
        await msg.reply('Попалась шл@шка')
        await msg.delete()

def register_other_handlers(dp:Dispatcher):
    dp.register_message_handler(bot_start,commands=['help', 'start'])
    dp.register_message_handler(mats)