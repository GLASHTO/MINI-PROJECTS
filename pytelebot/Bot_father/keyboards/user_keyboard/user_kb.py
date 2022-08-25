from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

# также можно группировать кнопки
# test = [InlineKeyboardButton(text='get_push',callback_data='https://www.youtube.com/' ),InlineKeyboardButton(text='url_youtube',url='https://www.youtube.com/')]
# insert - добавляет кнопкку в ту же строку
# add - устанавливает автоматом, на строку столько кнопок, сколько задано в параметре InlineMarkupKeyboard
# row - столько кнопок на строку сколько задано. Если их слишком много происходит перенос на след строку
# start_keyboard.add(*test)
# клавиатура
number = KeyboardButton('send number', request_contact=True)
geo = KeyboardButton('send location', request_location=True)

start = KeyboardButton('/start')
possibility = KeyboardButton('possibility')
one_time_keyboard_button = KeyboardButton('one_time_keyboard')
delete = KeyboardButton('delete_keyboard')

# вызов инлайн клавиатуры
inline_keyboard = KeyboardButton(text='inline_kb')

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.add(possibility).row(one_time_keyboard_button, inline_keyboard).row(number, geo).row(delete, start)
# одноразовая клавиатура
hide_keyboard = KeyboardButton('hide')
back_to_normalkey = KeyboardButton('back')
one_time_keyboard_ = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
one_time_keyboard_.row(hide_keyboard, back_to_normalkey)
