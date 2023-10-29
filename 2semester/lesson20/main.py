from aiogram import types, Dispatcher, Bot, executor

from db import db

TOKEN = "6422112698:AAG8opOLOuAsuXkYidb91gfr--a0qTzheiU"

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
	user = message.from_user

	first_name = user.first_name or str(user.id)
	last_name = user.last_name or ""
	if not db.user_exist_by_first_name(user.first_name):
		db.create_user(first_name=first_name, last_name=last_name)

	users = db.get_all_users()
	print(users)
	await message.answer("Hello from python")


def main():
	db.create_user_table()
	executor.start_polling(dispatcher=dp)


if __name__ == "__main__":
	main()
