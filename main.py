from config_data.config import load_config

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

config = load_config(None)

bot = Bot(token=config.tg_bot.token)

dp = Dispatcher()

@dp.message(CommandStart)
async def command_start(message : Message):
    await message.answer('Работает')






if __name__ == '__main__':
    dp.run_polling(bot)

