#%%
import logging
#%%
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

logger = logging.getLogger(__name__)

# Store bot screaming status
input_language = "English"
output_language = "Spanish"

# Pre-assign menu text
INPUT_MENU = "<b>Input Language</b>\n\n Please select the language you want to translate from."
OUTPUT_MENU = "<b>Output Language</b>\n\n Please select the language you wish to translate to."
DONE_MENU = "<b>Done!</b>\n Your translation languages have been set."

# Pre-assign button text
ENGLISH_BUTTON = "English"
SPANISH_BUTTON = "Spanish"

# Build keyboards
INPUT_MENU_MARKUP = InlineKeyboardMarkup([[
    InlineKeyboardButton(ENGLISH_BUTTON, callback_data=ENGLISH_BUTTON)
]])
OUTPUT_MENU_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton(SPANISH_BUTTON, callback_data=SPANISH_BUTTON)],
])


def echo(update: Update, context: CallbackContext) -> None:
    """
    This function would be added to the dispatcher as a handler for messages coming from the Bot API
    """

    # Print to console
    print(f'{update.message.from_user.first_name} wrote {update.message.text}')

    update.message.copy(update.message.chat_id)


def menu(update: Update, context: CallbackContext) -> None:
    """
    This handler sends a menu with the inline buttons we pre-assigned above
    """

    context.bot.send_message(
        update.message.from_user.id,
        INPUT_MENU,
        parse_mode=ParseMode.HTML,
        reply_markup=INPUT_MENU_MARKUP
    )


def button_tap(update: Update, context: CallbackContext) -> None:
    """
    This handler processes the inline buttons on the menu
    """

    data = update.callback_query.data
    text = ''
    markup = None

    if data==ENGLISH_BUTTON:
        input_language = data
        text = OUTPUT_MENU
        markup = OUTPUT_MENU_MARKUP

    elif data==SPANISH_BUTTON:
        output_language = data
        text = DONE_MENU
        markup = None

    # Close the query to end the client-side loading animation
    update.callback_query.answer()

    # Update message content with corresponding menu section
    update.callback_query.message.edit_text(
        text,
        ParseMode.HTML,
        reply_markup=markup
    )


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
