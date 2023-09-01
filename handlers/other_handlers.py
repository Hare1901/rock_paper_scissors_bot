from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

# Создаем объект роутера на весь модуль
router: Router = Router()

# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])