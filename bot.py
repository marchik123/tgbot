import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Берём токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Список случайных ответов
answers = [
    "Да.",
    "Нет.",
    "Лучше попробовать.",
    "Лучше не сейчас.",
    "Делай.",
    "Не делай."
]

# Функция-обработчик сообщений
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(answers))

def main():
    # Создаём приложение и добавляем обработчик
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    # Запускаем бота
    app.run_polling()

if name == "__main__":
    main()
