import telebot
import os
import validators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config_bot import config
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse

TOKEN = config['token']
bot = telebot.TeleBot(TOKEN)

chrome_options = Options()
chrome_options.add_argument('--headless')

@bot.message_handler(commands=['start'])
def hello_user(message):
    bot.send_message(message.chat.id, "Hello. This bot returns you an image of the site you specified.")

@bot.message_handler(commands=['help'])
def show_help(message):
    bot.send_message(message.chat.id, 'To get a screenshot of the site, use the /url command.\nExample: /url https://www.google.com')

@bot.message_handler(commands=['url'])
def get_screenshot(message):
    uid = message.chat.id
    url = ""
    try:
        url = message.text.split(' ')[1]
        image_name = f"{urlparse(url).netloc}.png"
    except IndexError:
        bot.send_message(uid, 'After the command /url, you need to enter a valid URL!')
        return
    if not validators.url(url):
        bot.send_message(uid, 'I could not open the URL. Try later.')
    else:
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1800)
        try:
            driver.get(url)
            png = driver.get_screenshot_as_png()
            im = Image.open(BytesIO(png))
            im.save(image_name, 'PNG')
            bot.send_document(uid, open(image_name, 'rb'))
            os.remove(image_name)
        except Exception as err:
            print(err)
        finally:
            driver.quit()

if __name__ == '__main__':
    bot.infinity_polling()
