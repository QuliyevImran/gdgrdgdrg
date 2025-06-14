from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import openai
import os



TELEGRAM_TOKEN = ""
OPENAI_API_KEY = ""

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет. Я карьерный помощник. Расскажи мне о своих интересах, сильных сторонах или чем ты хочешь заниматься, и я предложу тебе подходящую профессию"
    )

async def recommend_career(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "Ты карьерный консультант, помогающий подросткам и взрослым выбрать профессию."},
                {"role": "user", "content": f"Вот мой профиль: {user_input}. Какие профессии мне подходят?"}
            ],
            max_tokens=300
        )

        career_advice = response.choices[0].message.content.strip()
        await update.message.reply_text(f"Вот, что я советую:\n\n{career_advice}")

    except Exception as e:
        await update.message.reply_text("Упс! Что-то пошло не так. Попробуй ещё раз позже.")
        print(f"OpenAI error: {e}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recommend_career))

    print("Бот запущен")
    app.run_polling()
   
    log_to_db(user_id=str(message.from_user.id), name=entered_name, job=generated_job)
if __name__ == "__main__":
    main()
