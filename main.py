from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from files.mainmanager import *
import os

PORT = int(os.environ.get('PORT', 5000))
TOKEN = ''
HEROKUURL = ''

def echo_msg(msg):
	q = msg.split('\n')
	if q[0] == 'myclass':
		retVal = fetch_data(q[1],q[2])
	else:
		retVal = 'i don\'t think i know this query :/'
	return retVal

def start(update, context):
	sender = update.message.from_user
	# init_msg = ('User ID: ' + str(sender.id) 
	# 	+ '\nDisplay Name: ' + sender.full_name
	# 	+ '\nUsername: ' + sender.username
	# 	+ '\nIs bot: ' + str(sender.is_bot))
	init_msg = 'hi '+sender.usename+', type /help learn more'
	update.message.reply_text(init_msg)

def help(update, context):
	help_text = ('| help panel |\n============\n'+
		'Get binusmaya vicon list query: myclass[enter]username[enter]passworrd\n'
		+'\nmsg body example: \nmyclass\nyour.username\nsecret123\n'
		+'\n============')
	update.message.reply_text(help_text)

def echo(update, context):
	msg = echo_msg(update.message.text)
	update.message.reply_text(msg)

def main():
	updater = Updater(TOKEN)
	dpatcher = updater.dispatcher
	dpatcher.add_handler(CommandHandler('start', start))
	dpatcher.add_handler(CommandHandler('help', help))
	dpatcher.add_handler(MessageHandler(Filters.text, echo))

	updater.start_webhook(listen='0.0.0.0',
		port=int(PORT),
		url_path=TOKEN)
	updater.bot.set_webhook(HEROKUURL+TOKEN)
	
	# updater.start_polling()

	updater.idle()



if __name__ == '__main__':
	os.system('pyclean .')
	main()
