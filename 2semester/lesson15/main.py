# Кроки стану реєстрації:
# Ім'я
# Login
# Password
# Password 2

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from states import SignUp


TOKEN = "6422112698:AAG8opOLOuAsuXkYidb91gfr--a0qTzheiU"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands=["start"], state="*")
async def start_command(message: types.Message, state: FSMContext):
    await state.reset_state()
    await SignUp.name.set()
    await message.answer("Зареєструйтеся:")
    await message.answer("Введіть ваше ім'я:")


@dp.message_handler(commands=["cancel"], state="*")
async def cancel_command(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Охрана отмєна!")


@dp.message_handler(state=SignUp.name)
async def process_user_name(message: types.Message, state: FSMContext):
    name = message.text

    if len(name) < 2:
        return await message.answer("Ім'я не може бути коротше за 2 літери")

    async with state.proxy() as data:
        data["name"] = name

    await SignUp.login.set()
    await message.answer("Придумайте логін:")


@dp.message_handler(state=SignUp.login)
async def process_user_login(message: types.Message, state: FSMContext):
    login = message.text

    if len(login) < 5:
        return await message.answer("Login не може бути коротше за 5 символів")

    async with state.proxy() as data:
        data["login"] = login

    await SignUp.password1.set()
    await message.answer("Введіть пароль:")


@dp.message_handler(state=SignUp.password1)
async def process_user_password1(message: types.Message, state: FSMContext):
    password1 = message.text

    if len(password1) < 5:
        return await message.answer("Password1 не може бути коротше за 5 символів")

    async with state.proxy() as data:
        data["password1"] = password1

    await SignUp.password2.set()
    await message.answer("Підтвердіть пароль:")


@dp.message_handler(state=SignUp.password2)
async def process_user_password2(message: types.Message, state: FSMContext):
    password2 = message.text

    if len(password2) < 5:
        return await message.answer("Password2 не може бути коротше за 5 символів")

    async with state.proxy() as data:
        data["password2"] = password2

    data = await state.get_data()
    name = data['name']
    login = data['login']
    password1 = data['password1']
    password2 = data['password2']

    if password1 != password2:
        return await message.answer("Паролі не збігаються. Підтвердіть пароль:")

    await message.answer(f"Ваші дані:\n"
                         f"Name: {name}\n"
                         f"Login: {login}\n"
                         f"Password1: {password1}\n"
                         f"Password2: {password2}")
    await state.reset_state()


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True
    )
