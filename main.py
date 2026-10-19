import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# إعداد السجلات
logging.basicConfig(level=logging.INFO)

# جلب التوكين أوتوماتيكياً من متغيرات البيئة لحمايته
TOKEN = os.environ.get("BOT_TOKEN")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📋 قائمة الخدمات والأسعار", callback_data='services')],
        [InlineKeyboardButton("💬 طلب خدمة أو استفسار", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "أهلاً بك في بوت الخدمات الإلكترونية! 🚀\n"
        "كيف يمكنني مساعدتك اليوم؟ اختر من القائمة أدناه:",
        reply_markup=reply_markup
    )

# التفاعل مع الأزرار
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'services':
        await query.edit_message_text(
            "💰 **قائمة الخدمات والأسعار:**\n\n"
            "- تصميم وتطوير بوتات تلغرام مخصصة\n"
            "- أتمتة ردود المتاجر والقنوات\n"
            "- تنسيق الخدمات الأكاديمية والتقارير"
        )
    elif query.data == 'contact':
        await query.edit_message_text("📞 للتواصل المباشر مع المطوّر: أرسل استفسارك هنا.")

if __name__ == '__main__':
    if not TOKEN:
        print("خطأ: لم يتم ضبط BOT_TOKEN!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button_click))
        
        print("تم تشغيل البوت بنجاح...")
        app.run_polling()
