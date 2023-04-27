from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

import sys
sys.path.insert(0, '/bot')
from bot.keyboards.inline import reply_markup


@dp.message_handler(state=None, commands='showbutton')
async def bot_echo(message: types.Message):
    await message.answer('This is button', reply_markup=reply_markup)


@dp.callback_query_handler(text='button1pressed')
async def second_step(call: types.CallbackQuery):
    await call.message.answer("button pressed")


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
