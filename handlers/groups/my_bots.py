import asyncio
import datetime
import shutil
import subprocess
import sys
import psutil
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentTypes, CallbackQuery

from keyboards.inline.in_menu import in_menu_start, in_menu_mybots, in_menu_mybots_edit

from loader import dp, PAYMENTS_PROVIDER_TOKEN, bot
from utils.db_api.db import BotDB

@dp.callback_query_handler(lambda c: c.data.startswith('mybots'))
async def add_channel(call: CallbackQuery, state: FSMContext):
    __userid = call.from_user.id
    id_templ = call.data.split(' ')[-1]
    keyboard = await in_menu_mybots(__userid)


    await call.message.edit_text(text='🔘 Выберите вашего бота, с которым хотите выполнить действия',reply_markup=keyboard)



@dp.callback_query_handler(lambda c: c.data.startswith('editbot'))
async def add_channel(call: CallbackQuery, state: FSMContext):
    __userid = call.from_user.id
    apitoken = call.data.split(' ')[-1]

    keyboard = await in_menu_mybots_edit(__userid, apitoken)

    get_db_telegram = BotDB()
    bots_temp = get_db_telegram.get_bot_in_api_token(apitoken=apitoken)

    await call.message.edit_text(text=f'✍🏻 Выберите действие, которое хотите произвести с ботом\n'
                                      f'🔨 Username - bot: @{bots_temp["username"]}',reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('deletbot'))
async def delete_channel(call: CallbackQuery, state: FSMContext):
    __userid = call.from_user.id
    apitoken = call.data.split(' ')[-1]

    get_db_telegram = BotDB()
    bots_temp = get_db_telegram.get_bot_in_api_token(apitoken=apitoken)

    p = psutil.Process(int(bots_temp['pid']))
    p.terminate()
    get_db_telegram.del_bot_in_api_token(apitoken=apitoken)
    shutil.rmtree(f"bots/{apitoken.replace(':', '')}")
    keyboard = await in_menu_mybots(__userid)
    await call.message.edit_text(text='🔘 Выберите вашего бота, с которым хотите выполнить действия',reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('stopbot'))
async def stop_channel(call: CallbackQuery, state: FSMContext):
    __userid = call.from_user.id
    apitoken = call.data.split(' ')[-1]
    get_db_telegram = BotDB()
    bots_temp = get_db_telegram.get_bot_in_api_token(apitoken=apitoken)
    if bots_temp['status'] == 'True':
        get_db_telegram.edit_bots_status(apitoken=apitoken, status='False')
        p = psutil.Process(int(bots_temp['pid']))
        p.terminate()
        keyboard = await in_menu_mybots_edit(__userid, apitoken)
        await call.message.edit_text(text=f'🔴Бот остановлен\n\n✍🏻 Выберите действие, которое хотите произвести с ботом\n'
                                          f'🔨 Username - bot: @{bots_temp["username"]}', reply_markup=keyboard)
    else:
        get_db_telegram.edit_bots_status(apitoken=apitoken, status='True')
        dst_folder = f'bots/{apitoken.replace(":", "")}'
        print(f"{dst_folder}/app.py",apitoken,bots_temp['userid'])
        proc = subprocess.Popen(['python', f"{dst_folder}/app.py", apitoken, bots_temp['userid']],
                                shell=False)
        get_db_telegram.edit_pid_bot(apitoken=apitoken, pid=proc.pid)
        keyboard = await in_menu_mybots_edit(__userid, apitoken)
        await call.message.edit_text(
            text=f'🟢 Бот запущен\n\n✍🏻 Выберите действие, которое хотите произвести с ботом\n'
                 f'🔨 Username - bot: @{bots_temp["username"]}', reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('restartbot'))
async def restartbot_channel(call: CallbackQuery, state: FSMContext):
    __userid = call.from_user.id
    apitoken = call.data.split(' ')[-1]
    get_db_telegram = BotDB()
    bots_temp = get_db_telegram.get_bot_in_api_token(apitoken=apitoken)
    p = psutil.Process(int(bots_temp['pid']))
    p.terminate()
    await asyncio.sleep(2)
    dst_folder = f'bots/{apitoken.replace(":", "")}'
    proc = subprocess.Popen(['python', f"{dst_folder}/app.py", apitoken, bots_temp['userid']],
                            shell=False)
    get_db_telegram.edit_pid_bot(apitoken=apitoken, pid=proc.pid)
    keyboard = await in_menu_mybots_edit(__userid, apitoken)
    await call.message.edit_text(
        text=f'🟢 Бот перезапущен\n\n✍🏻 Выберите действие, которое хотите произвести с ботом\n'
             f'🔨 Username - bot: @{bots_temp["username"]}', reply_markup=keyboard)

