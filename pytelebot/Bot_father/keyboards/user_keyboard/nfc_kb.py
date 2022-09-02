from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


nfc_kb_stop = ReplyKeyboardMarkup(resize_keyboard=True)

nfc_stop = KeyboardButton('exit')


nfc_kb_stop.add(nfc_stop)

