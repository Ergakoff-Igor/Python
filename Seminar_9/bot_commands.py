from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def go(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Ok! Let\'s go together! {update.effective_user.first_name}')

async def sum (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(f'{a} + {b} = {a + b}')