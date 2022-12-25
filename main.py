from aiogram import Bot, Dispatcher, executor, types
from config import API 
from data import create_db,create_profile,get_user

async def start(_):
    await create_db()
    
    

bot = Bot(token = API)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    a = await get_user(user_id = message.from_user.id)
    if a == None: 
        await create_profile(user_id=message.from_user.id,user_name = message.from_user.first_name)
        await message.answer(f"Приветствуем вас! {(await get_user(user_id = message.from_user.id))[0]}")
    else: 
        await message.answer(f"Приветсвуем вас! {a[0]}")
        



        
    
    
    
    
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True,on_startup = start)    