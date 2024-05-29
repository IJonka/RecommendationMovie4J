import os
from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv, dotenv_values
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

load_dotenv()

# Проверяем наличие переменной окружения ADMINS
admin_env = os.getenv('ADMINS')
if admin_env is None:
    print("Ошибка: переменная окружения 'ADMINS' не установлена.")
    ADMINS = [229432828]
else:
    ADMINS = list(map(int, admin_env.split(', ')))

TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    raise ValueError("Ошибка: переменная окружения 'TOKEN' не установлена.")

movie_ganres = {
    "comedy": "Комедия",
    "fantasy": "Фантастика",
    "horror": "Ужасы",
    "action": "Боевик",
    "melodrama": "Мелодрама",
    "mystic": "Мистика",
    "detective": "Детектив",
    "military": "Военное"
}
movie_ganres_rus = {
    'комедия': 'comedy',
    'фантастика': 'fantasy',
    'ужасы': 'horror',
    'боевик': 'action',
    'мелодрама': 'melodrama',
    'мистика': 'mystic',
    'детектив': 'detective',
    'военное': 'military'
}

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)
