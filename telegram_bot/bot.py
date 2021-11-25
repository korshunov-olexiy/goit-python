import asyncio
import logging
import pathlib
import sys
from http import HTTPStatus
from urllib.parse import urlparse

import requests
from pyppeteer import launch
from telegram import Update
from telegram.ext import (CallbackContext, CommandHandler, Filters, MessageHandler, Updater)

from config_bot import config


TOKEN = config['token']
CURRENT_PATH = pathlib.Path(sys.argv[0]).parent.absolute()

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Send me the link to the site and I will return the screenshot to you.")

def check_site_exist(url: str) -> str:
    try:
        url_parts = urlparse(url)
        domain_name = url_parts.netloc
        request = requests.get(url).status_code
        return domain_name if request in [HTTPStatus.OK, HTTPStatus.MOVED_PERMANENTLY] else ''
    except:
        return ''

async def take_screenshot(url: str, screenshot_name: pathlib.Path) -> str:
    try:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        await page.screenshot({'path': screenshot_name})
        await browser.close()
        return True
    except Exception as err:
        print("::::::::::::::::::::::::::::::::::::: ERROR: ", err)
        return False

def send_screenshot(update: Update, context: CallbackContext):
    url = update.message.text
    print("::::::::::::::URL:", url)
    screenshot_name = check_site_exist(url)
    if screenshot_name:
        screenshot_name = CURRENT_PATH.joinpath(f"{screenshot_name}.png")
        print('::::::::::::::: IMAGE:', screenshot_name)
        #if asyncio.get_event_loop().run_until_complete(take_screenshot(url, screenshot_name)):
        if asyncio.run(take_screenshot(url, screenshot_name)):
            logging.info(f"image name: {screenshot_name}")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(screenshot_name, 'rb'), caption=f'This is screenshot of {url}')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Something went wrong. Please try again later.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, but couldn't open passed url.")


def main():
    #asyncio.get_event_loop().run_until_complete(main())
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.text & (~Filters.command), send_screenshot)
    dispatcher.add_handler(echo_handler)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    main()
