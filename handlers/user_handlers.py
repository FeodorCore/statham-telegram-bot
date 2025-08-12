import asyncio
import random
import json
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from DB.user_model import UserModel
from keyboards.inline_keyboards import rand_start_button, rand_supp_button
from AI.deepseek import generate
from AI.generate_ai import generate_loading
user_router = Router()

with open("Data/quotes.json", "r", encoding="utf-8") as f:
    quotes_data = json.load(f)

@user_router.message(Command("start"))
async def start(message: Message):
    user_info = message.from_user
    user = UserModel(
        user_id=user_info.id,
        username=user_info.username,
        first_name=user_info.first_name,
        last_name=user_info.last_name,
        registr_time=message.date.isoformat()
    )
    user_save = await user.save()
    greet_list = quotes_data["greetings"]

    await message.answer(
        random.choice(greet_list) if user_save == "updated" else greet_list[0],
        reply_markup=rand_start_button()
    )

@user_router.message(Command("help"))
async def help(message: Message):
    await message.answer("/start - запуск бота\n/quote - получить цитату")

@user_router.message(Command("quote"))
async def quote(message: Message):
    greet_list = quotes_data["receive_quotes"]
    generated = await generate_loading(message)

    if generated:
        await message.answer(generated, reply_markup=rand_supp_button())
        logging.info("Generated_AI")
    else:
        await message.answer(random.choice(greet_list), reply_markup=rand_supp_button())
        logging.info("Generated")
