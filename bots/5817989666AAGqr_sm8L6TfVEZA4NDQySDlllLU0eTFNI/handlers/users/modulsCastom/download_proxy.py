import os
import zipfile

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.start_menu import menu_back, menu_start
from loader import dp


@dp.message_handler(text='proxy', state='*')
async def get_proxy(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"⚡️Отправьте мне файл вашей <code>proxy.txt</code>",reply_markup=menu_back)
    await state.set_state('proxys')

@dp.message_handler(state='proxys',content_types=['document'])
async def dow_proxy(message, state: FSMContext):
    destination = rf"telegramusers/proxy.txt"
    await message.document.download(destination)

    try:
        with open(destination,'r+',encoding='utf-8') as file:
            count_proxy = [i.rstrip() for i in file.readlines() if len(i.split(':')) == 4]
    except Exception as E:
        count_proxy = 0
    await message.answer(f"🔥Отлично, мы получили файл <code>proxy.txt</code>\n\n"
                         f"Proxy: <b>{len(count_proxy)}</b>",reply_markup=menu_start)
