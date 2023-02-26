import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import token

bot = telegram.Bot(token=token)

updater = Updater(bot=bot, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome to my bot!")

def collect_data(update, context):
    # Check if the message contains a file
    if update.message.document or update.message.audio or update.message.video or update.message.photo:
        # Get the file ID and download the file
        if update.message.document:
            file_id = update.message.document.file_id
            file_extension = update.message.document.file_name.split(".")[-1]
        elif update.message.audio:
            file_id = update.message.audio.file_id
            file_extension = "mp3"
        elif update.message.video:
            file_id = update.message.video.file_id
            file_extension = "mp4"
        elif update.message.photo:
            file_id = update.message.photo[-1].file_id
            file_extension = "jpg"

        file = context.bot.get_file(file_id)
        file.download(f"./files/{update.message.message_id}.{file_extension}")
        context.bot.send_message(chat_id=update.message.chat_id, text="File saved!")
    # Otherwise, assume the message contains text
    else:
        data = update.message.text
        # Save the data to your database
        #save text into data.txt
        with open("data.txt", "a") as f:
            f.write(data + "\n")


        context.bot.send_message(chat_id=update.message.chat_id, text="Text saved!")



start_handler = CommandHandler('start', start)
collect_data_handler = MessageHandler(Filters.all & (~Filters.command), collect_data)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(collect_data_handler)

updater.start_polling()
updater.idle()

