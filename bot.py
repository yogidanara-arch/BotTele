from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = 8944265015:AAHIuHZX9zLAbUe5Q2Mw5RMIqbzSK6_tLDI

async def hitung(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text.strip()

    try:
        mm = float(pesan)

        if 0 <= mm <= 20:
            menit = 130
        elif 21 <= mm <= 40:
            menit = 216
        elif 41 <= mm <= 60:
            menit = 270
        elif 61 <= mm <= 80:
            menit = 295
        else:
            menit = 330

        jam = menit // 60
        sisa = menit % 60

        await update.message.reply_text(
            f"""🌧 Curah Hujan : {mm} mm

⏱ Durasi : {menit} menit
🕒 Setara : {jam} jam {sisa} menit"""
        )

    except:
        await update.message.reply_text(
            "Silakan masukkan angka saja.\n\nContoh:\n35"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, hitung)
)

print("Bot berjalan...")

app.run_polling()