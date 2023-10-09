from aiogram import types
from loader import dp
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.dispatcher.filters import Command
from filters.is_admin import IsAdmin
# scheduler = AsyncIOScheduler()
from .scheduler import scheduler


@dp.message_handler(IsAdmin(), Command("stop_question"))
async def stop_question(message: types.Message):
    scheduler.shutdown()
    await message.answer("So'z yuborish to'xtatildi. Boshlash uchun /start_question")