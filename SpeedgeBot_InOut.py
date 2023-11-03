import logging

from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

logger = logging.getLogger(__name__)

# Store bot screaming status
input_language = "English"
output_language = "Spanish"
screen = "input"

# Pre-assign menu text
INPUT_MENU = "<b>Input Language</b>\n\n Please select the language you want to translate from."
OUTPUT_MENU = "<b>Output Language</b>\n\n Please select the language you wish to translate to."
INDONE_MENU = "<b>Done!</b>\n Your input language have been set."
OUTDONE_MENU = "<b>Done!</b>\n Your output language have been set."

# Pre-assign button text
ENGLISH_BUTTON = "English"
SPANISH_BUTTON = "Español"
GERMAN_BUTTON = "Deutsch"
FRENCH_BUTTON = "Français"
CHINESE_BUTTON = "中文"

# Build keyboards
INPUT_MENU_MARKUP = InlineKeyboardMarkup([[
    InlineKeyboardButton(ENGLISH_BUTTON, callback_data=ENGLISH_BUTTON),
    InlineKeyboardButton(SPANISH_BUTTON, callback_data=SPANISH_BUTTON),
    InlineKeyboardButton(GERMAN_BUTTON, callback_data=GERMAN_BUTTON),
    InlineKeyboardButton(FRENCH_BUTTON, callback_data=FRENCH_BUTTON),
    InlineKeyboardButton(CHINESE_BUTTON, callback_data=CHINESE_BUTTON)
]])
OUTPUT_MENU_MARKUP = InlineKeyboardMarkup([[
    InlineKeyboardButton(ENGLISH_BUTTON, callback_data=ENGLISH_BUTTON),
    InlineKeyboardButton(SPANISH_BUTTON, callback_data=SPANISH_BUTTON),
    InlineKeyboardButton(GERMAN_BUTTON, callback_data=GERMAN_BUTTON),
    InlineKeyboardButton(FRENCH_BUTTON, callback_data=FRENCH_BUTTON),
    InlineKeyboardButton(CHINESE_BUTTON, callback_data=CHINESE_BUTTON)
]])


def echo(update: Update, context: CallbackContext) -> None:
    """
    This function would be added to the dispatcher as a handler for messages coming from the Bot API
    """

    # Print to console
    print(f'{update.message.from_user.first_name} wrote {update.message.text}')

    update.message.copy(update.message.chat_id)


def input_menu(update: Update, context: CallbackContext) -> None:
    """
    This handler sends a menu with the inline buttons we pre-assigned above
    """

    context.bot.send_message(
        update.message.from_user.id,
        INPUT_MENU,
        parse_mode=ParseMode.HTML,
        reply_markup=INPUT_MENU_MARKUP
    )
    

def output_menu(update: Update, context: CallbackContext) -> None:
    """
    This handler sends a menu with the inline buttons we pre-assigned above
    """

    context.bot.send_message(
        update.message.from_user.id,
        OUTPUT_MENU,
        parse_mode=ParseMode.HTML,
        reply_markup=OUTPUT_MENU_MARKUP
    )


def button_tap_input(update: Update, context: CallbackContext) -> None:
    """
    This handler processes the inline buttons on the menu
    """

    data = update.callback_query.data
    # text = ''
    # markup = None

    input_language = data
    text = INDONE_MENU
    print(f"Input language changed to {input_language}")


    # Close the query to end the client-side loading animation
    update.callback_query.answer()

    # Update message content with corresponding menu section
    update.callback_query.message.edit_text(
        text,
        ParseMode.HTML,
    )


def button_tap_output(update: Update, context: CallbackContext) -> None:
    """
    This handler processes the inline buttons on the menu
    """

    data = update.callback_query.data
    # text = ''
    # markup = None

    output_language = data
    text = OUTDONE_MENU
    print(f"Output language changed to {output_language}")

    # Close the query to end the client-side loading animation
    update.callback_query.answer()

    # Update message content with corresponding menu section
    update.callback_query.message.edit_text(
        text,
        ParseMode.HTML
    )


def main() -> None:
    updater = Updater("6555655872:AAE8rGE7twoNlOuIAOTDBUXuYBSfdL7_9x8")

    # Get the dispatcher to register handlers
    # Then, we register each handler and the conditions the update must meet to trigger it
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("InputLanguage", input_menu))
    dispatcher.add_handler(CommandHandler("OutputLanguage", output_menu))

    # Register handler for inline buttons
    dispatcher.add_handler(CallbackQueryHandler(button_tap_input))
    dispatcher.add_handler(CallbackQueryHandler(button_tap_output))


    # Echo any message that is not a command
    dispatcher.add_handler(MessageHandler(~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
