from create_bot import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher
# Админ
admin_id = None


class FSMNAdmin(StatesGroup):
    trial_write = State()  # пробная админка


# как пример проверки является ли пользователь админом,  метод  is_chat_admin при передаче true ,
# проверяет являтся ли пользователь написавший команду - админом
# важное дополнение - проверка работает только если сообщение отправлено в чат
# @dp.message_handler(lambda msg: msg.text.lower() == 'admin_try', is_chat_admin=True, state=None)
async def trial_write_admin(msg: types.Message, state: FSMContext):
    global admin_id
    await bot.send_message(msg.from_user.id, 'yes_sir?')
    await msg.delete()
    admin_id = msg.from_user.id
    if msg.from_user.id == admin_id:
        await FSMNAdmin.trial_write.set()


# @dp.message_handler(state=FSMNAdmin.trial_write)
async def try_ad(msg: types.Message, state: FSMContext):
    if msg.from_user.id == admin_id:
        async with state.proxy() as data:
            data['admin_id'] = admin_id
        cur_admin.execute('''INSERT INTO admin_info VALUES(?)''', tuple(data.values()))
        db_admin.commit()


# @dp.message_handler(state=None)
async def ad_try_end(msg: types.Message, state: FSMContext):
    if msg.from_user.id == admin_id:
        await state.finish()
        await bot.send_message(msg.from_user.id, f'Admin ID:\n{admin_id}')

def register_admin_handlers(dp:Dispatcher):
    dp.register_message_handler(trial_write_admin,lambda msg: msg.text.lower() == 'admin_try', is_chat_admin=True, state=None)
    dp.register_message_handler(try_ad,state=FSMNAdmin.trial_write)
    dp.register_message_handler(ad_try_end,state=None)