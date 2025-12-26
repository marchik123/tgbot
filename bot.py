import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "BOT_TOKEN"

answers = [
    "Да.",
    "Нет.",
    "Лучше попробовать.",
    "Лучше не сейчас.",
    "Делай.",
    "Не делай."
]

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(answers))

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Бот запущен. Ждёт сообщений...")
    app.run_polling()

if name == "main":
    main()
