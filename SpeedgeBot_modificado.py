import logging

from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# from general_function import charge_model, translate_function
# import telebot

logger = logging.getLogger(__name__)

# Store bot screaming status
output_language = "SP"

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
    print(f'{update.message.from_user.first_name} wrote {update.message.text}')
    print(f"Translated to {output_language}")

    # TOKEN = "6555655872:AAE8rGE7twoNlOuIAOTDBUXuYBSfdL7_9x8"
    # CHAT_ID = update.message.chat.id

    # bot = telebot.TeleBot(TOKEN)
    # file_info = bot.get_file(update.message.voice.file_id)
    # audio_file = bot.download_file(file_info.file_path)

    # with open(f'{CHAT_ID}.wav', 'wb') as new_file:
    #         new_file.write(audio_file)

    # translate_function(f"{CHAT_ID}.wav",CHAT_ID )

    update.message.copy(update.message.chat_id)


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


    leng_code = {"English":"EN", 
                 "Español":"SP", 
                 "Français":"FR", 
                 "Deutsch":"DE", 
                 "中文":"CH", 
                 "Português":"PT"}
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
