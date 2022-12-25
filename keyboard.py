from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
    
    
buttons_for_console = KeyboardButton("Playstation")

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(buttons_for_console)