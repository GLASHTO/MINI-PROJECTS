from .. import cur_vid, db_vid
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from .. import bot
from keyboards.user_keyboard.video_kb import video_kb
from keyboards.user_keyboard.user_kb import start_keyboard
from aiogram.types import ReplyKeyboardRemove
class For_vid(StatesGroup):
    vid = State()  # load the vid ID


# @dp.message_handler(lambda msg: msg.text.lower() == "load_the_video", state=None)
async def load_video(msg: types.Message):
    await For_vid.vid.set()
    await bot.send_message(msg.from_user.id, 'send the video',reply_markup=video_kb)


# @dp.message_handler(lambda msg: msg.text == 'Exit_from_vl')
async def video_cancel(msg:types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state is not None:
        return
    await state.finish()
    await msg.answer('minute...',reply_markup=ReplyKeyboardRemove())
    await msg.answer('Ok,mtrfcr',reply_markup=start_keyboard)

# @dp.message_handler(content_types=['video'], state=For_vid.vid)
async def get_the_videos(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['video'] = msg.video.file_id
        cur_vid.execute('''INSERT INTO video_id VALUES(?)''', tuple(data.values()))
        db_vid.commit()
        await bot.send_message(msg.from_user.id, f'video loaded, ID:\n{data["video"]}')


# @dp.message_handler(lambda msg: msg.text == "DONE", state=For_vid.vid)
async def finish_loading(msg: types.Message, state: FSMContext):
    await msg.answer('all videos loaded',reply_markup=start_keyboard)
    await state.finish()


def register_video_handler(dp: Dispatcher):
    dp.register_message_handler(load_video, lambda msg: msg.text.lower() == "load_the_video", state=None)
    dp.register_message_handler(video_cancel,lambda msg: msg.text == 'Exit_from_vl',state='* ')
    dp.register_message_handler(get_the_videos, content_types=['video'], state=For_vid.vid)
    dp.register_message_handler(finish_loading, lambda msg: msg.text == "DONE", state=For_vid.vid)
