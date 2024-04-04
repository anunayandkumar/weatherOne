from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import weather
import weatherBot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}. To get weather update use command /weather <location> . Ex : /weather Kolkata')
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    title = " ".join(context.args)
    weatherResult = weatherBot.getResults('Kolkata')
    await update.message.reply_text(weatherResult)


app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("weather", weather))


app.run_polling()