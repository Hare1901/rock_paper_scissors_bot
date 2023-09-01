from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

#Кнопки с согласием или нет
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU["yes_button"])
buttno_no: KeyboardButton = KeyboardButton(text=LEXICON_RU["no_button"])

#Инициализация билдера с кнопками да/нет, и добавляем  в него кнопки с аргументом
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, buttno_no, width=2)

#Сщдаем клавиатуру с добавленными кнопками
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
) 


# ------- Создаем игровую клавиатуру без использования билдера -------

#Создаем необходимыен кнопки
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])


# Создаем клавиатуру с кнопками 
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[
                                                    [button_1],
                                                    [button_2],
                                                    [button_3],
                                                    ],
                                                    resize_keyboard=True)