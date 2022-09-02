import sqlite3
from create_bot import bot
db_nfc = sqlite3.connect(r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\pytelebot\Bot_father\db\nfc.db')
db_admin = sqlite3.connect(r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\pytelebot\Bot_father\db\admin.db')
db_vid = sqlite3.connect(r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\pytelebot\Bot_father\db\video.db')

cur_nfc = db_nfc.cursor()
cur_admin = db_admin.cursor()
cur_vid = db_vid.cursor()

async def get_data(msg, db, table):
    for data in db.execute(f'SELECT * FROM {table}').fetchall():
        await bot.send_message(msg.from_user.id, data[0])