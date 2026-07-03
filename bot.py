import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv(8944265015:AAHIuHZX9zLAbUe5Q2Mw5RMIqbzSK6_tLDI)

async def hitung(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text.strip()

    try:
        mm = float(pesan)

        if mm <= 20:
            menit = 130
        elif mm <= 40:
            menit = 216
        elif mm <= 60:
            menit = 270
        elif mm <= 80:
            menit = 295
        else:
            menit = 330

        jam = menit // 60
        sisa = menit % 60

        await update.message.reply_text(
            f"""🌧 Curah Hujan : {mm:.0f} mm

⏱ Durasi : {menit} menit
🕒 Setara : {jam} jam {sisa} menit"""
        )

    except ValueError:
        await update.message.reply_text(
            "Masukkan angka curah hujan.\n\nContoh:\n35"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, hitung)
)

print("Bot berjalan...")

app.run_polling()