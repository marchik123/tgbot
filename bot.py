import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8526040986:AAHpP6zzX15dTS5tRY3DUNdLCey7OldWu2E"

answers = [
    "Да.",
    "Нет.",
    "Лучше попробовать.",
    "Лучше не сейчас.",
    "Делай.",
    "Не делай."
]

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(random.choice(answers))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.run_polling()
