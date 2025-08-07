from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def default_commands_user(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начало работы с ботом"),
        BotCommand(command="help", description="Как пользоваться?"),
        BotCommand(command="quote", description="Получить цитату")
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())