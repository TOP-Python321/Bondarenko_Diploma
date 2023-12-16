from config_data.config import BOT_TOKEN


from aiogram import Bot, Dispatcher

from aiogram.filters import Command, CommandStart
from aiogram.types import Message


bot = Bot(token= BOT_TOKEN)

dp = Dispatcher()

@dp.message(CommandStart)
async def command_start(message : Message):
    await message.answer('Работает')






if __name__ == '__main__':
    dp.run_polling(bot)

