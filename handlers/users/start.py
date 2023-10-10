from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import random
from loader import dp, db
from data.config import CHANNEL_ID, ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # add user to database
    db.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name)
    
    await message.answer("Assalomu alaykum xush kelibsiz")
    
