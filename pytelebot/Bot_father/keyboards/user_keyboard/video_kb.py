from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

video_kb = ReplyKeyboardMarkup(resize_keyboard=True)

done=KeyboardButton("DONE")
exit_vid = KeyboardButton('Exit_from_vl')
video_kb.row(done,exit_vid)