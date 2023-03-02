from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from config import BOT_TOKEN, OW_TOKEN
from openweather_api_scripts import get_weather


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def start(msg: Message):
    await msg.answer("Xohlagan bir shaharning nomini yozing")


@dp.message_handler()
async def answering_to_user(msg: Message):
    city = msg.text

    text = await get_weather(city, OW_TOKEN)

    await msg.reply(text)



if __name__ == '__main__':
    from aiogram.utils.executor import start_polling
    start_polling(dp)