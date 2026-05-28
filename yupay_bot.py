import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Добро пожаловать в *YuPay*!\n\n"
        "💱 *1 CNY* = 11.6 RUB\n"
        "💵 *1 USD* = 6.42 CNY\n"
        "➖➖➖➖➖➖➖➖➖➖\n"
        "✅ Комиссия: *0%*\n"
        "💰 Сумма: *300¥ – 10.000¥*\n"
        "🕐 Работаем: *08:00 – 23:00*\n\n"
        "Нажмите кнопку ниже для обмена 👇"
    )
    keyboard = [[InlineKeyboardButton("💸 Exchange", callback_data="exchange")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "exchange":
        await query.message.reply_text("🔄 Введите сумму в юанях (¥):")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
