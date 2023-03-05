from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="sessions"),
            KeyboardButton(text="proxy"),
            KeyboardButton(text="chat"),
        ],
        [
            KeyboardButton(text="settings"),
            KeyboardButton(text="forward"),
            KeyboardButton(text="text"),
        ],
    ],
    resize_keyboard=True
)
menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="back"),
        ],
    ],
    resize_keyboard=True
)