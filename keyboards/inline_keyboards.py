from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random

import json


with open("Data/quotes.json", "r", encoding="utf-8") as f:
    quotes_data = json.load(f)
    

def rand_start_button() -> InlineKeyboardMarkup:
    greet_list = quotes_data["get_quote"]
    text = random.choice(greet_list)
    kb = InlineKeyboardBuilder()
    kb.button(text=text, callback_data="start_quotes")
    kb.adjust(1)
    return kb.as_markup()


def rand_supp_button() -> InlineKeyboardMarkup:
    greet_list = quotes_data["supplement"]
    return InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{random.choice(greet_list)}", callback_data="another")]
])
