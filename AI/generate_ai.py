import asyncio
from aiogram.types import Message

from AI.deepseek import generate  


async def generate_loading(message: Message,loading_text: str = "Цитата генерируется", timeout: int = 90, interval: int = 1) -> str | None:

    loading_msg = await message.answer(loading_text)
    dots = [".", "..", "..."]
    generate_task = asyncio.create_task(generate())

    for i in range(timeout // interval):
        await asyncio.sleep(interval)
        await loading_msg.edit_text(f"{loading_text} {dots[i % len(dots)]}")
        if generate_task.done():
            break

    result = await generate_task
    await loading_msg.delete()
    return result
