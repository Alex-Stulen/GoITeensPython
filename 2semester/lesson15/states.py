from aiogram.dispatcher.filters.state import StatesGroup, State


class SignUp(StatesGroup):
    name = State()
    login = State()
    password1 = State()
    password2 = State()
