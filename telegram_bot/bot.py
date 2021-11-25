from config_bot import config
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from pyppeteer import launch
import logging


TOKEN = config['token']
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Send me the link to the site and I will return the screenshot to you.")

async def take_screenshot(url: str):
    browser = await launch()
    page = await browser.newPage()
    screenshot_name = f"{page.url}.png"
    await page.goto(url)
    await page.screenshot({'path': screenshot_name})
    await browser.close()
    return screenshot_name

def send_screenshot(update: Update, context: CallbackContext):
    #context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    url = update.message.text
    img_name = take_screenshot(url)
    logging.info(f"image name: {img_name}")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(img_name, 'rb'), caption=f'This is screenshot of {url}')

echo_handler = MessageHandler(Filters.text & (~Filters.command), send_screenshot)
dispatcher.add_handler(echo_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

if __name__ == '__main__':
    #asyncio.get_event_loop().run_until_complete(main())
    updater.start_polling()
