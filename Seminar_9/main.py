import os
os.system('cls')
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
TOKEN = "5413184694:AAFRDgmz5WipWGnMcXCJHn8wZSP68U0dWdU"


app = ApplicationBuilder().token(TOKEN).build()
print("Server start")
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("go", go))
app.add_handler(CommandHandler("sum", sum))
app.run_polling()
print("Server stop")

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from bot_commands import *

# updater = Updater("5413184694:AAFRDgmz5WipWGnMcXCJHn8wZSP68U0dWdU")

# updater.dispatcher.add_handler(CommandHandler('hello', hi_command))
# updater.dispatcher.add_handler(CommandHandler('sum', sum_command))


# print('server start')
# updater.start_polling()
# updater.idle()
# print('server stop')


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token("5413184694:AAFRDgmz5WipWGnMcXCJHn8wZSP68U0dWdU").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()


# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from bot_token import TOKEN


# welcome_speech = \
#     """Привет, я тестовый бот!
# Я могу выполнять пока всего две комманды:
# здороваться по команде /hello и складывать два чиисла.
# Чтобы сложить 2 числа пришли мне комманду /sum и два числа после пробела.
# например /sum 2 3"""


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     mess = update.message.text
#     items = mess.split()
#     a, b = int(items[1]), int(items[2])
#     await update.message.reply_text(f'{a} + {b} = {a + b}')


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_speech)

# app = ApplicationBuilder().token(TOKEN).build()

# # start_handler = CommandHandler('start', start)
# app.add_handler(CommandHandler('start', start))
# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(CommandHandler("sum", sum_command))

# app.run_polling()