from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6244968995:AAHOtA-cq_Jx7L0618yaXhMkg4K2r2GQPNM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(lambda m: m.text == "Привіт")
async def send_hello(message: types.Message):
    await message.answer("Привіт :)")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
