from telegram import InlineKeyboardButton, ReplyKeyboardMarkup

def generateKeyboard(buttons: list[InlineKeyboardButton]) -> ReplyKeyboardMarkup:
   return ReplyKeyboardMarkup(buttons, resize_keyboard=True, is_persistent=True)
