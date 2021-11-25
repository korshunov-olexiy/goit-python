import telebot
import os
import validators
from selenium import webdriver
from config_bot import config
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse


TOKEN = config['token']
bot = telebot.TeleBot(TOKEN)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--no-sandbox')


@bot.message_handler(commands=['start'])
def hello_user(message):
    bot.send_message(message.chat.id, "Hello. This bot returns you an image of the site you specified.")

@bot.message_handler(commands=['help'])
def show_help(message):
    bot.send_message(message.chat.id, 'To get a screenshot of the site, use the /getphoto command.\nExample: /getphoto https://www.google.com')

@bot.message_handler(commands=['getphoto'])
def get_screenshot(message):
    uid = message.chat.id
    url = ""
    try:
        url = message.text.split(' ')[1]
        image_name = f"{urlparse(url).netloc}.png"
    except IndexError:
        bot.send_message(uid, 'After the command /getphoto, you need to enter a valid URL!')
        return
    if not validators.url(url):
        bot.send_message(uid, 'I could not open the URL. Try later.')
    else:
        driver = webdriver.Chrome(chrome_options = options)
        driver.set_window_size(1920, 1800)
        driver.execute_script("document.body.style.zoom='250%'")
        driver.get(url)
        png = driver.get_screenshot_as_png()
        driver.quit()
        im = Image.open(BytesIO(png))
        im.save(image_name)
        bot.send_document(uid, data=open(image_name, 'rb'))
        os.remove(image_name)


if __name__ == '__main__':
    bot.infinity_polling()
