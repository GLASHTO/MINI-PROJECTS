from aiogram.utils import executor
from aiogram import  Bot,types,Dispatcher
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
import hashlib
bot=Bot('2001852541:AAGNXaOYmaoyBDZDhj3JDZc74zsRooqIGvc')
dp=Dispatcher(bot)
@dp.inline_handler()
async def inline_bot(query:types.InlineQuery):
    text=query.query or 'echo'
    link = 'https://www.youtube.com/results?search_query='+text
    result_id:str=hashlib.md5(text.encode()).hexdigest()
    articles = [InlineQueryResultArticle(
        id=result_id,
        title='Youtube',
        url=link,
        input_message_content=InputTextMessageContent(message_text=link)
    )]
    await query.answer(articles, cache_time=1, is_personal=True)




executor.start_polling(dp,skip_updates=True)