from aiogram import types
from loader import dp, db
from aiogram.dispatcher.filters import Command
from filters.is_admin import IsAdmin


@dp.message_handler(Command("start"), IsAdmin())
async def stop_question(message: types.Message):
    await message.answer("Xush kelibsiz")
    db.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name)
    