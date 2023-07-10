import logging
import os
import constants
from utils.keyboard import generateKeyboard

from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import filters, Application, CommandHandler, ContextTypes, MessageHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
TOKEN = os.environ["TOKEN"]

# -------------------------------- KEYBOARD ------------------------------------
testing_keyboard_button = InlineKeyboardButton(constants.TESTING_BUTTON_TEXT)
payment_button = InlineKeyboardButton(constants.PAYMENT_BUTTON_TEXT)
back_button = InlineKeyboardButton(constants.BACK_BUTTON_TEXT)
successfully_payment_button = InlineKeyboardButton(constants.SUCCESSFULLY_PAYMENT_TEXT)

async def keyboard_message_handler(update: Update, context:  ContextTypes.DEFAULT_TYPE):
    if constants.TESTING_BUTTON_TEXT in update.message.text:
        await testing(update, context)
    if constants.PAYMENT_BUTTON_TEXT in update.message.text:
        await send_payment(update, context)
    if constants.SUCCESSFULLY_PAYMENT_TEXT in update.message.text:
        await confirm_payment(update, context)
    if constants.BACK_BUTTON_TEXT in update.message.text:
        await start(update, context)

# -------------------------------- BOT ACTIONS ------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    buttons = [[testing_keyboard_button]]
    keyboard = generateKeyboard(buttons)
    await context.bot.send_message(chat_id=chat_id, text=f'Добро пожаловать, @{update.effective_chat.username}!\nLorem Ipsum Lorem Ipsum', reply_markup=keyboard)

async def testing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    buttons = [[payment_button], [back_button]]
    keyboard = generateKeyboard(buttons)
    await context.bot.send_message(chat_id=chat_id, text="Тестирование Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem", reply_markup=keyboard)

async def send_payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    buttons = [[successfully_payment_button]]
    keyboard = generateKeyboard(buttons)
    await context.bot.send_message(chat_id=chat_id, text=f'Ссылка для оплаты example.com', reply_markup=keyboard)

async def confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    buttons = [[back_button]]
    keyboard = generateKeyboard(buttons)
    await context.bot.send_message(chat_id=chat_id, text=f'Отлично, ожидаем средства, далее высылаем тест!', reply_markup=keyboard)

# -------------------------------- SETUP ------------------------------------
def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, keyboard_message_handler))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()