from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

politic_reply_markup = InlineKeyboardMarkup()
economic_reply_markup = InlineKeyboardMarkup()

politic1 = InlineKeyboardButton(text='1', callback_data='p0')
politic2 = InlineKeyboardButton(text='2', callback_data='p1')
politic3 = InlineKeyboardButton(text='3', callback_data='p2')
politic4 = InlineKeyboardButton(text='4', callback_data='p3')

economic1 = InlineKeyboardButton(text='1', callback_data='e0')
economic2 = InlineKeyboardButton(text='2', callback_data='e1')
economic3 = InlineKeyboardButton(text='3', callback_data='e2')
economic4 = InlineKeyboardButton(text='4', callback_data='e3')


politic_reply_markup.add(politic1, politic2, politic3, politic4)
economic_reply_markup.add(economic1, economic2, economic3, economic4)
