from aiogram.dispatcher.filters.state import StatesGroup, State


class Flow(StatesGroup):
    RegisterState = State()
