from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from constants import API_TOKEN
from responses import sample_responses
import datetime
import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! I’m Reo10bot 🤖 — here to chat, motivate, or joke with you! Try typing anything or use /help")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Welcome message\n"
        "/help - List of commands\n"
        "/joke - Get a funny joke 😂\n"
        "/motivate - Get a motivational quote 💪\n"
        "/time - Get the current time 🕒\n"
        "/date - Get today's date 📅"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = sample_responses(text)
    await update.message.reply_text(response)

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    ]
    await update.message.reply_text(random.choice(jokes))

async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [
        "Believe in yourself. You are braver than you think! 💫",
        "Keep going. Everything you need will come to you at the perfect time. 🌈",
        "Small steps every day lead to big results. 💪"
    ]
    await update.message.reply_text(random.choice(quotes))

async def get_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time_now = datetime.datetime.now().strftime('%H:%M:%S')
    await update.message.reply_text(f"⏰ Current time: {time_now}")

async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date_today = datetime.datetime.now().strftime('%A, %d %B %Y')
    await update.message.reply_text(f"📅 Today's date: {date_today}")

def main():
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("motivate", motivate))
    app.add_handler(CommandHandler("time", get_time))
    app.add_handler(CommandHandler("date", get_date))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Reo10bot is running with enhanced features...")
    app.run_polling()

if __name__ == "__main__":
    main()
