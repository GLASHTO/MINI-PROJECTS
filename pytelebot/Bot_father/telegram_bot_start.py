from aiogram.utils import executor
from create_bot import dp
from db import db_vid, db_admin, db_nfc, cur_nfc, cur_admin, cur_vid
from handlers import admin
from handlers import user
from handlers import other


# то что происходит перед стартом бота
def on_startup():
    cur_vid.execute('''CREATE TABLE IF NOT EXISTS video_id(
    video TEXT
    )
    ''')
    cur_admin.execute('''CREATE TABLE IF NOT EXISTS admin_info(
    trial_write VARCHAR)
    ''')
    cur_nfc.execute('''CREATE TABLE IF NOT EXISTS nfc_info(
    name VARCHAR,
    photo TEXT,
    description TEXT
    )''')
    db_admin.commit()
    db_vid.commit()
    db_nfc.commit()
    print('Холо проснулась ,услужи ей)')


# регистрация хэндлеров, модуль с пустым хэндлером также расположен снизу
admin.register_admin_handlers(dp)
user.register_user_handlers(dp)
other.register_other_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
