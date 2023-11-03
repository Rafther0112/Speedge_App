import logging
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton,ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from flask import Flask, request, jsonify, send_file
import os
from general_function import charge_model, charge_model_translation, translate_function
import telebot

logger = logging.getLogger(__name__)
charge_model()
traductor_model = charge_model_translation()

# Store bot screaming status
output_language = "en"

# Pre-assign menu text
MENU = "<b>Output Language</b>\n\n Please select the language you want to translate to."
DONE_MENU = "<b>Done!</b>\n Your translation language have been set."

# Pre-assign button text
ENGLISH_BUTTON = "English"
SPANISH_BUTTON = "Español"
FRENCH_BUTTON = "Français"
GERMAN_BUTTON = "Deutsch"
CHINESE_BUTTON = "中文"
PORTUGUESE_BUTTON = "Português"

# Build keyboards
MENU_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton(ENGLISH_BUTTON, callback_data=ENGLISH_BUTTON)],
    [InlineKeyboardButton(SPANISH_BUTTON, callback_data=SPANISH_BUTTON)],
    [InlineKeyboardButton(FRENCH_BUTTON, callback_data=FRENCH_BUTTON)],
    [InlineKeyboardButton(GERMAN_BUTTON, callback_data=GERMAN_BUTTON)],
    # [InlineKeyboardButton(CHINESE_BUTTON, callback_data=CHINESE_BUTTON)]
    # [InlineKeyboardButton(PORTUGUESE_BUTTON, callback_data=PORTUGUESE_BUTTON)]
])

def echo(update: Update, context: CallbackContext) -> None:
    """
    This function would be added to the dispatcher as a handler for messages coming from the Bot API
    """

    # Print to console
    print(f'{update.message.from_user.first_name} sent a message')

    if not update.message.voice == None:
        TOKEN = "6555655872:AAE8rGE7twoNlOuIAOTDBUXuYBSfdL7_9x8"
        CHAT_ID = update.message.chat.id

        bot = telebot.TeleBot(TOKEN)
        file_info = bot.get_file(update.message.voice.file_id)
        audio_file = bot.download_file(file_info.file_path)

        with open(f'{CHAT_ID}.wav', 'wb') as new_file:
                new_file.write(audio_file)

        translate_function(f"{CHAT_ID}.wav",CHAT_ID,  "all", output_language)
        bot.send_audio(chat_id=CHAT_ID, audio=open(f"final_{CHAT_ID}.mp3", 'rb'))
        
    else:

        TOKEN = "6555655872:AAE8rGE7twoNlOuIAOTDBUXuYBSfdL7_9x8"
        CHAT_ID = update.message.chat.id
        bot = telebot.TeleBot(TOKEN)

        traduccion_target = traductor_model.translate(update.message.text, target_lang= output_language)
        print(traduccion_target)
        bot.send_message(chat_id=CHAT_ID, text = traduccion_target)
        
def menu(update: Update, context: CallbackContext) -> None:
    """
    This handler sends a menu with the inline buttons we pre-assigned above
    """

    context.bot.send_message(
        update.message.from_user.id,
        MENU,
        parse_mode=ParseMode.HTML,
        reply_markup=MENU_MARKUP
    )
    
def button_tap(update: Update, context: CallbackContext) -> None:
    """
    This handler processes the inline buttons on the menu
    """

    data = update.callback_query.data
    # text = ''
    # markup = None

    global output_language

    text = DONE_MENU
    print(f"Languages changed to {data}")


    leng_code = {"English":"en", 
                 "Español":"sp", 
                 "Français":"fr", 
                 "Deutsch":"de", 
                 "中文":"ch", 
                 "Português":"pt"}
    output_language = leng_code[data]


    # Close the query to end the client-side loading animation
    update.callback_query.answer()

    # Update message content with corresponding menu section
    update.callback_query.message.edit_text(
        text,
        ParseMode.HTML,
    )
    
    return output_language

def main() -> None:
    updater = Updater("6555655872:AAE8rGE7twoNlOuIAOTDBUXuYBSfdL7_9x8")

    # Get the dispatcher to register handlers
    # Then, we register each handler and the conditions the update must meet to trigger it
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("Language", menu))

    # Register handler for inline buttons
    dispatcher.add_handler(CallbackQueryHandler(button_tap))


    # Echo any message that is not a command
    dispatcher.add_handler(MessageHandler(~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
