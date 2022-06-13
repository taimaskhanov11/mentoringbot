import logging

from aiogram import Dispatcher, Router
from loguru import logger
router = Router()

log = logging.getLogger()
async def error_handler(update, exception):
    log.exception(exception)

    # try:
    #     logger.exception(exception)
    # except:
    return True


def register_error(dp: Dispatcher):
    dp.include_router(router)
    router.errors.register(error_handler)
