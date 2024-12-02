import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Вставьте сюда ваш токен
TOKEN = '7965997384:AAFwm0qNa9h1PhPQ4Ldn_6tW0fiQw1kXSP8'

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Функция, обрабатывающая команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш бот.')

# Функция для отправки сообщения
def send_message(chat_id: str, text: str) -> None:
    context.bot.send_message(chat_id=chat_id, text=text)

def main():
    # Создаем Updater и передаем ему токен бота.
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()

    # Ожидание завершения
    updater.idle()

if __name__ == '__main__':
    main()