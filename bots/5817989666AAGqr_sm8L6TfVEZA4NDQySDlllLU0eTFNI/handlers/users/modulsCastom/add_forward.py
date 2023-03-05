import os
import zipfile

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.start_menu import menu_back, menu_start
from loader import dp, api_token
from utils.db_api.db import BotDB


@dp.message_handler(text='forward', state='*')
async def get_forward(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"⚡️Отправьте мне чаты(forward) в формате:\n\n<code>@test1\n"
                         f"https://t.me/astroplannerbot</code>",reply_markup=menu_back)
    await state.set_state('forward')


@dp.message_handler(state='forward')
async def get_chat(message: types.Message, state: FSMContext):
    try:
        await state.finish()
        forward = message.text
        get_db_telegram = BotDB()
        get_db_telegram.add_forward_in_user(apitoken=api_token,forward=forward)

        count = forward.count('\n') + 1
        await message.answer(f"🔥Отлично, мы получили чаты(forward): <code>{count}</code>", reply_markup=menu_start)
    except Exception as E:
        await state.finish()
        await message.answer(f'🔴Произошла фатальная ошибка: {E}')