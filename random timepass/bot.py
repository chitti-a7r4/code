from telegram.client import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# A dictionary to store chat pairs
chat_pairs = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to Random Chat! Use /chat to start chatting with a random user.')

def chat(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id in chat_pairs:
        update.message.reply_text('You are already in a chat.')
        return
    
    # Find a user to chat with
    available_users = [user for user in chat_pairs if chat_pairs[user] is None]
    if available_users:
        partner = random.choice(available_users)
        chat_pairs[user_id] = partner
        chat_pairs[partner] = user_id
        update.message.reply_text(f'You are now chatting with a random user.')
        context.bot.send_message(chat_id=partner, text=f'You are now chatting with a random user.')
    else:
        chat_pairs[user_id] = None
        update.message.reply_text('Waiting for a random user to chat with...')

def message_handler(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id in chat_pairs and chat_pairs[user_id]:
        partner = chat_pairs[user_id]
        context.bot.send_message(chat_id=partner, text=update.message.text)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("chat", chat))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
