import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

RESPONSE_LINK = "https://your-link-here.com"  # عدل الرابط هنا

async def send_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"هذا هو الرابط المطلوب:\n{RESPONSE_LINK}")

async def empty_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم إعادة ضبط الأوامر (محايدة)")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    commands = ["start", "ban", "login", "camera", "device", "share", "help"]
    for cmd in commands:
        app.add_handler(CommandHandler(cmd, send_link))
    app.add_handler(CommandHandler("empty", empty_command))

    print("البوت يعمل الآن...")
    app.run_polling()
