from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# التوكن الخاص بك
TOKEN = "7103221259:AAFngxvMCQ4AlI-JVGIn10RZKdgmOzm9s3w"
# آيدي تيليجرام تبعك
YOUR_CHAT_ID = 7220184605

# روابط كل الأوامر
COMMAND_LINKS = {
    "start": "https://example.com/start",
    "ban": "https://example.com/ban",
    "login": "https://example.com/login",
    "camera": "https://example.com/camera",
    "device": "https://example.com/device",
    "share": "https://example.com/share",
    "help": """🧾 قائمة الأوامر:
/start - بدء البوت
/ban - تنفيذ التبنيد
/login - تسجيل الدخول
/camera - التقاط من الكاميرا
/device - معلومات الجهاز
/share - رابط المشاركة
/empty - حذف الأوامر
""",
    "empty": "✅ تم حذف قائمة الأوامر مؤقتًا."
}

# دالة ترسل الرابط أو الرد المناسب حسب الأمر
async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text.lstrip("/").split()[0]
    if update.effective_chat.id != YOUR_CHAT_ID:
        await update.message.reply_text("🚫 هذا البوت مخصص فقط لصاحب الحساب.")
        return

    reply = COMMAND_LINKS.get(command, "❌ الأمر غير معروف.")
    await update.message.reply_text(reply)

# تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    for cmd in COMMAND_LINKS:
        app.add_handler(CommandHandler(cmd, handle_command))

    print("✅ البوت يعمل الآن...")
    app.run_polling()
