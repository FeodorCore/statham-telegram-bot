import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot_commands.user_commands import default_commands_user

from config import BOT_TOKEN 
from handlers.user_handlers import user_router
from handlers.callback_handlers import callback_router
from DB.user_model import UserRepository 

async def main():
    logging.basicConfig(level=logging.INFO) 

    db_ini = UserRepository()
    db_ini.initialize_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(user_router)
    dp.include_router(callback_router)
    logging.info("Бот запускается...")
    
    await default_commands_user(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())