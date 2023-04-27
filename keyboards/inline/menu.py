from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

reply_markup = InlineKeyboardMarkup()

reply_markup.add(InlineKeyboardButton(text='Button', callback_data='button1pressed'))