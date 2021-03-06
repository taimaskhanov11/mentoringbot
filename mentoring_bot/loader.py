from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from loguru import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import ssl
from mentoring_bot.config.config import config
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
logger.info(config.bot.token)
bot = Bot(token=config.bot.token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

# i18n = setup_lang_middleware(dp)
# _ = i18n.gettext


def _(text):
    return text
