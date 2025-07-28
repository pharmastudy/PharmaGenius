
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from token import TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["/pharmacy_notes", "/gk_quiz"], ["/math", "/mock_test"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("📚 Welcome to Pharma Study Bot! Choose a section below:", reply_markup=reply_markup)

async def pharmacy_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📘 D.Pharm Notes\n📙 B.Pharm Notes\n📗 M.Pharm Notes\n(Coming Soon...)")

async def gk_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 GK Quiz Coming Soon...")

async def math(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📐 Math Practice Coming Soon...")

async def mock_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 GPAT Mock Test Coming Soon...")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pharmacy_notes", pharmacy_notes))
    app.add_handler(CommandHandler("gk_quiz", gk_quiz))
    app.add_handler(CommandHandler("math", math))
    app.add_handler(CommandHandler("mock_test", mock_test))
    print("Bot is running...")
    app.run_polling()
