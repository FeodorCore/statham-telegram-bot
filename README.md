# 🤖 Statham-telegram-bot

## 🚀 Installation

To install and run the bot, follow these steps:

1. Clone the repository:
```
git clone https://github.com/your-username/bot-for-generating-quotes.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Set the necessary environment variables:
   - `BOT_TOKEN`: Your bot token obtained from the BotFather.
   - `AI_KEY`: Your API key for the AI model used for generating quotes.

4. Run the bot:
```
python bot.py
```

## 🎮 Usage

The bot provides the following commands:

- `/start`: Starts the bot and greets the user.
- `/help`: Displays information on how to use the bot.
- `/quote`: Generates and sends a random quote to the user.

When the user interacts with the bot, they can request a new quote by clicking the "Another" button.

## 🔌 API

The bot uses the following APIs:

- **Aiogram**: A modern and fast API for building Telegram bots.
- **Deepseek**: An AI model used for generating quotes.

## 🖼 Preview

Here’s how the bot looks in action:

<img src="assets/screenshot.png" alt="Bot Screenshot" width="400"/>

## 📁 Directory Hierarchy
```
|—— bot.py
|—— .gitignore
|—— AI
|    |—— deepseek.py
|    |—— generate_ai.py
|—— bot.py
|—— bot_commands
|    |—— user_commands.py
|    |—— __init__.py
|—— Data
|    |—— quotes.json
|    |—— __init__.py
|—— DB
|    |—— user_model.py
|    |—— __init__.py
|—— handlers
|    |—— callback_handlers.py
|    |—— user_handlers.py
|    |—— __init__.py
|—— keyboards
|    |—— inline_keyboards.py
|    |—— __init__.py
|—— requirements.txt
|—— __init__.py
```
## ✅ Conclusion

The bot is ready to use. Install it, run it, and try out the commands.  