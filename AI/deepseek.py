import httpx
import logging
import json
from config import AI_KEY

with open("Data/quotes.json", "r", encoding="utf-8") as f:
    quotes_data = json.load(f)

greet_list = quotes_data["receive_quotes"]

async def generate():
    try:
        headers = {
            "Authorization": f"Bearer {AI_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek/deepseek-r1-0528:free",
            "messages": [
                {
                    "role": "system",
                    "content": (f"Твоя задача — давать цитату, вот пример цитат: {greet_list}. "
                                "По примеру придумай цитату на такую же тематику! Выдай только цитату, без пояснений, просто подходящий эмодзи и текст.")
                },
                {
                    "role": "user",
                    "content": "Дай цитату похожую схожую с примером"
                }
            ]
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )

        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        logging.error(f"Ошибка генерации цитаты: {e}")
        return None
