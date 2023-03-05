import logging
import sys

from aiogram import Dispatcher

from data.config import ADMINS
from utils.db_api.db import BotDB


async def on_startup_notify(dp: Dispatcher):

    apitoken = sys.argv[1:][0]
    userid = sys.argv[1:][1]
    bot_dict = dict(await dp.bot.me)
    botname = bot_dict['first_name']
    username = bot_dict['username']
    get_db_telegram = BotDB()
    get_db_telegram.add_bots_in_bd(userid,apitoken,botname,username)
    for admin in ADMINS:
        try:
            try:
                await dp.bot.send_message(admin, "Бот Запущен")
            except Exception as E:
                print(E)

        except Exception as err:
            logging.exception(err)
