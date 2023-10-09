from aiogram import types
from loader import dp, db
from aiogram.dispatcher.filters import Command
from filters.is_admin import IsAdmin
import random 
from data.config import CHANNEL_ID
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def give_question():
    random_word_id = random.randint(2, 3000)
    if db.check_word(random_word_id):
        random_word_id = random.randint(2, 3000)
    word = db.get_word(random_word_id)
    numbers = [random.randint(2, 3000) for _ in range(3)]
    options = []
    for i in numbers:
        vars = db.get_word(i)[2]
        options.append(vars)
    question = f"'{word[1]}' means? level: {word[4]}"
    options.append(word[2])
    
    explain = f"{word[1]} - {word[2]} ({word[3]})"

    options = random.sample(options, len(options))
    correct_answer = options.index(word[2])
    print(options)
    poll = await dp.bot.send_poll(
        CHANNEL_ID,
        question,
        options=options,
        type=types.PollType.QUIZ,  # Set poll type to QUIZ
        correct_option_id=correct_answer,  # Index of the correct answer in the options list
        is_anonymous=True,
        explanation=explain,  # Explanation for the correct answer
        explanation_parse_mode=types.ParseMode.MARKDOWN
    )
    db.add_todays_word(word[0])

scheduler = AsyncIOScheduler()


@dp.message_handler(IsAdmin(), Command("start_question"))
async def start_question(message: types.Message):
    db.todays_words_table()
    scheduler.add_job(give_question, trigger='interval', seconds=5)
    if not scheduler.running:
        scheduler.start()
        for i in scheduler.get_jobs():
            await message.answer(f"So'zlarni yuborish boshlandi.\nTo'xtatish uchun /stop_question \nKeyingisi : {i.next_run_time}")
    else:
        scheduler.resume()
        for i in scheduler.get_jobs():
            await message.answer(f"So'zlarni yuborish boshlandi. Keyingisi : {i.next_run_time}")


