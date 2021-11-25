from config_bot import config
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
import telebot
#import constants
#from telebot import types
TOKEN = config['token']
bot = telebot.TeleBot(TOKEN)
print([b for b in dir(bot) if not b.startswith('__')])

def bot_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.poll()
