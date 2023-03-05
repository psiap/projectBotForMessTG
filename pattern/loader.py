import sys

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from data import config


api_token = sys.argv[1:][0] #"5817989666:AAGqr_sm8L6TfVEZA4NDQySDlllLU0eTFNI"
bot = Bot(token=sys.argv[1:][0], parse_mode=types.ParseMode.HTML)
#bot = Bot(token="5817989666:AAGqr_sm8L6TfVEZA4NDQySDlllLU0eTFNI", parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


