import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, PollAnswerHandler, ContextTypes

#TOKEN = os.getenv("8042821970:AAHsCv3OoKKf-JkyNzb9-kuJpPpehK-kgbI")



# Quiz data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Rome"],
        "answer": 0  # index of correct option
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 1
    }
]

# Track user progress
user_data = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data[user_id] = {"index": 0, "score": 0}
    await send_quiz(update.effective_chat.id, context, user_id)

# Send quiz question
async def send_quiz(chat_id, context: ContextTypes.DEFAULT_TYPE, user_id):
    index = user_data[user_id]["index"]

    if index < len(quiz_data):
        question = quiz_data[index]
        await context.bot.send_poll(
            chat_id=chat_id,
            question=f"Q{index+1}: {question['question']}",
            options=question["choices"],
            type='quiz',
            correct_option_id=question["answer"],
            is_anonymous=False
        )
    else:
        score = user_data[user_id]["score"]
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"✅ Quiz finished!\nYour score: {score}/{len(quiz_data)}"
        )
        del user_data[user_id]

# Handle quiz answer
async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poll_answer = update.poll_answer
    user_id = poll_answer.user.id
    selected = poll_answer.option_ids[0]

    if user_id in user_data:
        index = user_data[user_id]["index"]
        correct = quiz_data[index]["answer"]

        if selected == correct:
            user_data[user_id]["score"] += 1

        user_data[user_id]["index"] += 1
        await send_quiz(user_id, context, user_id)

# Replace with your actual token
TOKEN = "8042821970:AAHsCv3OoKKf-JkyNzb9-kuJpPpehK-kgbI"


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(PollAnswerHandler(handle_poll_answer))

print("🤖 Bot is running...")
app.run_polling()
