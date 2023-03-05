import os
import zipfile

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.start_menu import menu_back, menu_start
from loader import dp


@dp.message_handler(text='sessions', state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"⚡️Отправьте мне файл <code>.zip</code>",reply_markup=menu_back)
    await state.set_state('sessions')

@dp.message_handler(state='sessions',content_types=['document'])
async def add_channel_get_photo(message, state: FSMContext):
    name_of_file = f'zip_{message.from_user.id}.zip'
    await message.document.download(name_of_file)
    try:
        session_path = f'telegramusers'
        file = zipfile.ZipFile(name_of_file)
        file.extractall(session_path)
        file.close()
        os.remove(name_of_file)
        sessions = os.listdir(session_path)
        sessions = [i for i in sessions if 'session' in i]
        await message.answer(f"🔥Отлично, мы получили .session в колличестве - <code>{len(sessions)}</code>",reply_markup=menu_start)

        await state.finish()
    except Exception as E:
        await message.answer(f"🔴 Повторите попытку {E}")