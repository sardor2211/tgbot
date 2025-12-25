from aiogram import Bot, Dispatcher, executor, types

TOKEN = "7584685507:AAE2U2Pw0nNoksLlg1vGUTWfle5J6elJPkI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Salom! Men oddiy Telegram botman 🤖")

@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)