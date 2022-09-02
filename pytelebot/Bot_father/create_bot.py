from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from configuration.config import TOKEN

# память ОЗУ
storage = MemoryStorage()

# бот принимающиц значение токена
bot = Bot(token=TOKEN)
# обработчик действий пользователя
dp = Dispatcher(bot, storage=storage)


