from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from filters.is_admin import IsAdmin


@dp.message_handler(Command("start"), IsAdmin())
async def stop_question(message: types.Message):
    await message.answer("Xush kelibsiz")