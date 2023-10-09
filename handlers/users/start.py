from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import random
from loader import dp, db
from data.config import CHANNEL_ID, ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalomu alaykum xush kelibsiz")
    
