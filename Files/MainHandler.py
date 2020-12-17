from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
class MainHandler():
	def start(update, context):
	    update.message.reply_text('Hi!')

	def help(update, context):
	    update.message.reply_text('Help!')

	def echo(update, context):
	    update.message.reply_text(update.message.text)