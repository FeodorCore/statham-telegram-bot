import json
import random
import logging
from aiogram import Router, types
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards import rand_supp_button
from AI.generate_ai import generate_loading


callback_router = Router()

with open("Data/quotes.json", "r", encoding="utf-8") as f:
    quotes_data = json.load(f)


@callback_router.callback_query(lambda c: c.data == "start_quotes")
async def zitata_start(callback: CallbackQuery):
    await callback.answer()
    greet_list = quotes_data["receive_quotes"]
    generated = await generate_loading(callback.message)
    logging.info("Generated_AI" if generated else "Generated")
    await callback.message.answer(generated if generated else random.choice(greet_list), reply_markup=rand_supp_button())
    await callback.message.edit_reply_markup(reply_markup=None)

@callback_router.callback_query(lambda c: c.data == "another")
async def zitata_another(callback: CallbackQuery):
    await callback.answer()
    greet_list = quotes_data["receive_quotes"]
    generated = await generate_loading(callback.message)
    logging.info("Generated_AI" if generated else "Generated")
    await callback.message.answer(generated if generated else random.choice(greet_list), reply_markup=rand_supp_button())
    await callback.message.edit_reply_markup(reply_markup=None)
    