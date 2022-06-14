import asyncio
import logging

from aiogram import Bot
from aiogram.types import BotCommand
from loguru import logger

from mentoring_bot.apps.bot.handlers.admin.admin_menu import register_admin
from mentoring_bot.apps.bot.handlers.common import register_common
from mentoring_bot.apps.bot.handlers.errors.errors_handlers import register_error
from mentoring_bot.config.config import config
from mentoring_bot.config.logg_settings import init_logging
from mentoring_bot.db import init_db
from mentoring_bot.loader import bot, dp, scheduler


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Главное меню"),
        BotCommand(command="/admin", description="Админ меню")
    ]
    await bot.set_my_commands(commands)


async def start():
    # Настройка логирования
    init_logging(
        old_logger=True,
        level="TRACE",
        # old_level=logging.DEBUG,
        old_level=logging.INFO,
        steaming=False,
        write=True,
    )

    # dp.startup.register(on_startup)
    # dp.shutdown.register(on_shutdown)

    # Установка команд бота
    await set_commands(bot)

    # Инициализация бд
    await init_db(**config.db.dict())
    scheduler.start()
    # Меню админа
    register_admin(dp)
    # Регистрация хэндлеров
    register_common(dp)
    register_error(dp)

    # Регистрация middleware

    # Регистрация фильтров
    while True:
        try:
            await dp.start_polling(bot, skip_updates=True)
        except Exception as e:
            logger.exception(e)
            await asyncio.sleep(5)


def main():
    asyncio.run(start())


if __name__ == "__main__":
    main()
