from aiogram import Router, types
from aiogram.types import CallbackQuery

import json


from keyboards.inline_keyboards import rand_supp_button

import random

callback_router = Router()

with open("Data/quotes.json", "r", encoding="utf-8") as f:
    quotes_data = json.load(f)


@callback_router.callback_query(lambda c: c.data == "start_quotes")
async def zitata_start(callback: CallbackQuery):
    greet_list = quotes_data["receive_quotes"]
    await callback.message.answer(random.choice(greet_list), reply_markup=rand_supp_button())
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer()

@callback_router.callback_query(lambda c: c.data == "another")
async def zitata_another(callback: CallbackQuery):
    greet_list = quotes_data["receive_quotes"]
    await callback.message.answer(random.choice(greet_list), reply_markup=rand_supp_button())
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer()
    