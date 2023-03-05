import os
import zipfile

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.start_menu import menu_back, menu_start
from loader import dp, api_token
from utils.db_api.db import BotDB


@dp.message_handler(text='chat', state='*')
async def get_chat(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"⚡️Отправьте мне чаты в формате:\n\n<code>@test1\n"
                         f"https://t.me/astroplannerbot</code>",reply_markup=menu_back)
    await state.set_state('chat')


@dp.message_handler(state='chat')
async def get_chat(message: types.Message, state: FSMContext):
    try:
        await state.finish()
        chat = message.text
        get_db_telegram = BotDB()
        get_db_telegram.add_chat_in_user(apitoken=api_token,chat=chat)

        count = chat.count('\n') + 1
        await message.answer(f"🔥Отлично, мы получили чаты <code>{count}</code>", reply_markup=menu_start)
    except Exception as E:
        await state.finish()
        await message.answer(f'🔴Произошла фатальная ошибка: {E}')