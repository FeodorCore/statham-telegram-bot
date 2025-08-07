from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message 

from DB.insert_users_db import User

from keyboards.inline_keyboards import rand_start_button, rand_supp_button


import random
import json

user_router = Router()

with open("Data/quotes.json", "r", encoding="utf-8") as f:
    quotes_data = json.load(f)

@user_router.message(Command("start"))
async def start(message: Message):
    user_inf = message.from_user
    user = User(user_inf.id, user_inf.username, user_inf.first_name, user_inf.last_name)
    user_db = user.save()
    greet_list = quotes_data["greetings"]
    await message.answer(random.choice(greet_list) if user_db else greet_list[0], reply_markup=rand_start_button())


@user_router.message(Command("help"))
async def help(message: Message):
    await message.answer("/start - запуск бота\n"
                         "/quote - получить цитату"
                        )


@user_router.message(Command("quote"))
async def quote(message: Message):
    greet_list = quotes_data["receive_quotes"]
    await message.answer(random.choice(greet_list), reply_markup=rand_supp_button())
