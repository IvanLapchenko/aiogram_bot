from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

red = KeyboardButton(text='Red')
yellow = KeyboardButton(text='Yellow')
green = KeyboardButton(text='Green')

lights_all = ReplyKeyboardMarkup(resize_keyboard=True).add(red, yellow, green)
red_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(red)
yellow_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(yellow)
green_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(green)