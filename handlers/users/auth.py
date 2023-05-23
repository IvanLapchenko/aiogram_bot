from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from bot.keyboards.default import auth_kb
from bot.states import Flow

from loader import dp


@dp.message_handler(CommandStart(), state=Flow.RegisterState)
async def start_handler(message: types.Message):
    await message.answer('You\'ve already registered:)')


@dp.message_handler(CommandStart())
async def start_handler(message: types.Message):
    await message.answer('You can\'n use this bot unless you are not registered',
                         reply_markup=auth_kb.share_phone_keyboard)


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(message: types.Message):
    if message.contact.user_id != message.from_id:
        await message.answer('It\'s not you')
    else:
        await Flow.RegisterState.set()
        await message.answer(f'Welcome, {message.from_user.full_name}')
