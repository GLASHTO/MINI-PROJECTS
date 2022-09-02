from aiogram import Dispatcher,types
import json
import string
arr_with_mats = json.load(
    open(r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\pytelebot\Bot_father\pycache\damn.json'))

async def mats(msg: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in msg.text.split(' ')}.intersection(
            set(arr_with_mats)) != set():
        await msg.reply('Попалась шл@шка')
        await msg.delete()


def register_mat_handler(dp:Dispatcher):
    dp.register_message_handler(mats)