import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Добро пожаловать в *YuPay*!\n\n"
        "💱 *1 CNY* = 11.93 RUB\n"
        "💵 *1 USD* = 6.42 CNY\n"
        "➖➖➖➖➖➖➖➖➖➖\n"
        "✅ Комиссия: *0%*\n"
        "💰 Сумма: *300¥ – 10.000¥*\n"
        "🕐 Работаем: *08:00 – 23:00*\n\n"
        "Нажмите «Exchange» для обмена"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
