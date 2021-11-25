from config_bot import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=config['token'])
dp = Dispatcher(bot)
