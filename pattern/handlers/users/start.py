import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile

from keyboards.default import menu_start
from loader import dp, api_token, bot
from utils.db_api.db import BotDB


async def get_info_from_user(user_id):
    # Get information session
    try:
        sessions = len([i for i in os.listdir(f'telegramusers/') if 'session' in i])
    except Exception as E:
        sessions = 0
    # Get information proxy
    try:
        with open(rf"telegramusers/proxy.txt", 'r+', encoding='utf-8') as file:
            proxys = len([i.rstrip() for i in file.readlines() if len(i.split(':')) == 4])
    except Exception as E:
        proxys = 0

    # Get information chats
    get_db_telegram = BotDB()
    data = get_db_telegram.get_information(apitoken=api_token)
    try:
        chats = data['chat'].count('\n') + 1
    except Exception as E:
        chats = 0

    try:
        forwards = data['forward'].count('\n') + 1
    except Exception as E:
        forwards = 0
    try:
        text_u = data['text'][:10] + '...'
    except Exception as E:
        text_u = 'None'

    try:
        img_u = data['imgpath']
    except Exception as E:
        img_u = 'None'
    return sessions, proxys, chats, forwards,text_u,img_u

@dp.message_handler(text='back',state='*')
@dp.message_handler(CommandStart(),state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    sessions, proxys, chats, forwards, text_u, img_u = await get_info_from_user(message.from_user.id)

    if img_u == 'None':
        await message.answer(f"<b>Стартовые параметры бота</b>\n\n"
                             f"Status: 🟢\n\n"
                             f"📡 Sessions: <b>{sessions}</b>\n\n"
                             f"📟 Proxy: <b>{proxys}</b>\n\n"
                             f"🪬 Chat: {chats}\n\n"
                             f"🧿 Forward: {forwards}\n\n"
                             f"📩 Text: {text_u}",
                             reply_markup=menu_start)
    else:
        photo = InputFile(
            img_u
        )
        await bot.send_photo(chat_id=message.chat.id, photo=photo,caption=f"<b>Стартовые параметры бота</b>\n\n"
                             f"Status: 🟢\n\n"
                             f"📡 Sessions: <b>{sessions}</b>\n\n"
                             f"📟 Proxy: <b>{proxys}</b>\n\n"
                             f"🪬 Chat: {chats}\n\n"
                             f"🧿 Forward: {forwards}\n\n"
                             f"📩 Text: {text_u}\n\n"
                             f"🖼 Img path: {img_u}",
                             reply_markup=menu_start)