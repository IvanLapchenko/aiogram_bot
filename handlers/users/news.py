import sys
from loader import dp
from aiogram import types
from bot.keyboards.default import reply_markup as reply
from bot.keyboards.inline import economic_reply_markup, politic_reply_markup

sys.path.insert(0, '/bot')


@dp.message_handler(state=None, commands='whattoread')
async def bot_echo(message: types.Message):
    await message.answer('Choose topic', reply_markup=reply)


@dp.message_handler(state=None, text='Economic news')
async def handle_economic_news(message: types.Message):
    await message.answer('Choose the article', reply_markup=economic_reply_markup)


@dp.message_handler(state=None, text='Politic news')
async def handle_economic_news(message: types.Message):
    await message.answer('Choose the article', reply_markup=politic_reply_markup)


# @dp.message_handler(state=None, commands='showinline')
# async def bot_echo(message: types.Message):
#     await message.answer('This is button', reply_markup=inline)


@dp.callback_query_handler(text='button1pressed')
async def second_step(call: types.CallbackQuery):
    await call.message.answer("button pressed")