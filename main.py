import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# إعداد السجلات
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("BOT_TOKEN")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📋 قائمة الخدمات والأسعار", callback_data='services')],
        [InlineKeyboardButton("💬 طلب خدمة أو استفسار", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "أهلاً بك في بوت المهندس سيد للخدمات البرمجية والحلول التقنية! 🚀\n"
        "كيف يمكنني مساعدتك اليوم؟ اختر من القائمة أدناه:",
        reply_markup=reply_markup
    )

# التفاعل مع الضغط على الأزرار
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'services':
        await query.edit_message_text(
            "💰 **قائمة الخدمات المتاحة:**\n\n"
            "1️⃣ تصميم وبناء بوتات تلغرام مخصصة (متاجر، أتمتة، خدمات).\n"
            "2️⃣ ربط البوتات بسيرفرات تعمل 24/7 أونلاين.\n"
            "3️⃣ حلول أتمتة الردود وإدارة القنوات والمجموعات.\n\n"
            "لطلب أي خدمة، اكتب استفسارك مباشرة هنا وسيتم الرد عليك فوراً!"
        )
    elif query.data == 'contact':
        await query.edit_message_text(
            "✍️ **اكتب استفسارك أو طلبك الآن مباشرة في الشات:**\n"
            "سيصل استفسارك وسيتم الرد عليك في أقرب وقت ممكن."
        )

# استقبال رسائل الزبائن
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user = update.message.from_user
    
    # رد تلقائي لتأكيد الاستلام للعميل
    await update.message.reply_text("شكرًا لتواصلك! تم استلام رسالتك وسيتم الرد عليك قريباً جداً.")
    
    # تسجيل الرسالة
    print(f"رسالة جديدة من {user.first_name} (@{user.username}): {user_text}")

if __name__ == '__main__':
    if not TOKEN:
        print("خطأ: لم يتم ضبط BOT_TOKEN!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button_click))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        print("تم تشغيل البوت المطور بنجاح...")
        app.run_polling()
