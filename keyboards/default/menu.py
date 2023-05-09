from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)

economic_news = KeyboardButton(text='Economic news')
politic_news = KeyboardButton(text='EU news')


reply_markup.add(economic_news, politic_news)
