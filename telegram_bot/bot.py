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
#dp = Dispatcher(bot)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call): #your call
    UserID = str(call.message.chat.id)

    if call.data == 'PhotoTEXT': 
       @bot.message_handler(content_types=['text'])
       def SetTEXTonPHOTO(message):  # THIS FUNCTION
           sent = bot.send_message(message.chat.id,'send me text')
           bot.register_next_step_handler(sent, TextONphoto)

           def TextONphoto(message): #Thsi function add text on photo
              im = Image.open('UserData/Files/photos/not_converted/'+UserID+'.jpg')
              idraw = ImageDraw.Draw(im)
              text = message.text
              font = ImageFont.truetype("arial.ttf", size=18)
              idraw.text((10, 10), text, font=font)  
              im.save('UserData/Files/photos/converted/'+UserID+'.jpg')
              im.show()

    SetTEXTonPHOTO(call.message) #just run your function
    with open('UserData/Files/photos/converted/'+UserID+'.jpg', 'rb') as file:
         bot.send_document(UserID,file)
