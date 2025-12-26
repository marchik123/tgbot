import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

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
    app.run_polling()

if name == "__main__":
    main()
