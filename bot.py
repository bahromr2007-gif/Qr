import os
import telebot
import qrcode
import io

# Bot tokenini environment variable dan olamiz
BOT_TOKEN = "8365235218:AAH9v2x2LqbdWQUJFP875k4fikr5zn-KBT0"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🤖 QR Kod Botiga xush kelibsiz!\n\nMatn yuboring — men QR kod yasab beraman!")

@bot.message_handler(func=lambda message: True)
def qrcode_text(message):
    try:
        # QR kod yaratish
        img = qrcode.make(message.text)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        
        # QR kodni yuborish
        bot.send_photo(message.chat.id, buf, caption=f"📱 QR kod tayyor: {message.text}")
        
    except Exception as e:
        bot.reply_to(message, f"❌ Xatolik yuz berdi: {str(e)}")

if __name__ == "__main__":
    print("🚀 Bot ishga tushdi...")
    bot.infinity_polling()