from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.keyboards.default import states_kb
from bot.states import Lights

from loader import dp


@dp.message_handler(commands='traffic_lights_on')
async def traffic_lights_on(message: types.Message):
    await Lights.StateOn.set()
    await message.answer('You turned on traffic lights. Choose the light you want to turn on.',
                         reply_markup=states_kb.lights_all)


@dp.message_handler(text='Red', state=Lights.StateOn)
async def red_handler(message: types.Message):
    await Lights.StateRed.set()
    await message.answer('You turned on red light. Now you can turn yellow on.',
                         reply_markup=states_kb.yellow_kb)


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


