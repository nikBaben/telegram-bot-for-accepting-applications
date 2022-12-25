from aiogram import Bot, Dispatcher, executor, types
from config import API 
from data import create_db

async def start(_):
    await create_db()
    
    

bot = Bot(token = API)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.answer("Приветствуем вас!")
    
    
    
    
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True,on_startup = start)    