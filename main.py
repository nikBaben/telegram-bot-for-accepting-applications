from aiogram import Bot, Dispatcher, executor, types
from config import API 


bot = Bot(token = API)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.answer("Приветствуем вас!")
    
    
    
    
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)    