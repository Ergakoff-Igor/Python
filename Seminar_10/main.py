from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
from config import TOKEN
from time import sleep
from game import Game
from random import randint


async def message_processing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка сырого текста в чате"""
    if update.message.text[0] != '/':
        if game.gamestatus:
            # запущена игра
            # ход игрока
            try:
                matches = int(update.message.text)
            except:
                await update.message.reply_text('Я не понял ваш ответ. Напишите цифрой, какую позицию вы выбираете.')
                return
            if not 0 < matches < 10:
                await update.message.reply_text('Вы вышли за границы игрового поля')
                return
            game.action_player(matches)
            if game.check_game_state():
                await update.message.reply_text(f'{game.showMatrix()} \nПоздравляю вас, вы выиграли')
                game.stop()
                return
            if game.check_drawn_game():
                await update.message.reply_text(f'{game.showMatrix()} \nНичья')
                game.stop()
                return                
            message = f'Ваш ход: \n{game.showMatrix()}'
            print(game.showMatrix())
            await update.message.reply_text(message)
            sleep(1)
            # ход компьютера
            game.action_cpu()
            message = f'Ход компьютера: \n{game.showMatrix()}'
            print(game.showMatrix())
            await update.message.reply_text(message)
            sleep(1)
            if game.check_game_state():
                message = f'Я выиграл'
                await update.message.reply_text(message)
                game.stop()
                return
            if game.check_drawn_game():
                await update.message.reply_text(f'{game.showMatrix()} \nНичья')
                game.stop()
                return  
            message = 'Ваш ход'
            await update.message.reply_text(message)
            return


async def gamestart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """старт игры"""
    if not game.gamestatus:
        game.start()
        message = game.help
        await update.message.reply_text(message)
        message = f'Игра началась.\nИгровое поле: \n{game.showMatrix()}\n'
        await update.message.reply_text(message)
        print(game.showMatrix())
        if randint(1, 100) > 50:
            message = 'Я хожу первый\n'
            await update.message.reply_text(message)
            game.action_cpu()
            message = f'Ход компьютера: \n{game.showMatrix()}'
            print(game.showMatrix())
            await update.message.reply_text(message)
        else:
            message = 'Ваш ход'
            await update.message.reply_text(message)


app = ApplicationBuilder().token(TOKEN).build()
print ('Server start')
app.add_handler(CommandHandler("GAME", gamestart))

app.add_handler(MessageHandler(None, message_processing))
game = Game()  # создаем игру

app.run_polling()
print ('Server stop')