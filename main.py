import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Files.MainHandler import *
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1425460282:AAGHnd__02UAKvnNC3estkF6Rv8MEbpi8fI'

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    mh = new MainHandler()
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", mh.start))
    dp.add_handler(CommandHandler("help", mh.help))
    dp.add_handler(CommandHandler("about", mh.help))
    dp.add_handler(MessageHandler(Filters.text, mh.echo))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://desolate-beyond-35820.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()