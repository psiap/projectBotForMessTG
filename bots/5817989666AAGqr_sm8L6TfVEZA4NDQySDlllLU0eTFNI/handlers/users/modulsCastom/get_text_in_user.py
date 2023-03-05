import os
import zipfile

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.start_menu import menu_back, menu_start
from loader import dp, api_token
from utils.db_api.db import BotDB


@dp.message_handler(text='text', state='*')
async def get_chat(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"⚡️Отправьте мне текст одним сообщением, если захотите с картинкой",reply_markup=menu_back)
    await state.set_state('text')

@dp.message_handler(state='text',content_types=['photo'])
async def add_channel_get_photo(message, state: FSMContext):
    img_path = rf'data/1.png'
    text_caption = 'None'
    await message.photo[-1].download(img_path)
    if message.caption:
        text_caption = message.caption

    get_db_telegram = BotDB()
    get_db_telegram.add_text_in_user(apitoken=api_token, text=text_caption,imgpath=img_path)
    await message.answer(f"🔥Отлично, мы получили текст",reply_markup=menu_start)
    await state.finish()


@dp.message_handler(state='text')
async def add_channel_get_photo(message, state: FSMContext):
    img_path = rf'None'
    text_caption = message.text

    get_db_telegram = BotDB()
    get_db_telegram.add_text_in_user(apitoken=api_token, text=text_caption,imgpath=img_path)
    await message.answer(f"🔥Отлично, мы получили текст",reply_markup=menu_start)
    await state.finish()