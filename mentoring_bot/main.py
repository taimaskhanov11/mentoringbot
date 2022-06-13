import asyncio
import logging

from aiogram import Bot
from aiogram.types import BotCommand
from mentoring_bot.apps.bot.handlers.common import register_common
from mentoring_bot.apps.bot.handlers.errors.errors_handlers import register_error
from mentoring_bot.config.config import config
from mentoring_bot.config.logg_settings import init_logging
from mentoring_bot.db import init_db
from mentoring_bot.loader import bot, dp, scheduler

import ssl


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Главное меню")
    ]
    await bot.set_my_commands(commands)


async def start():
    # Настройка логирования
    init_logging(
        old_logger=True,
        level="TRACE",
        # old_level=logging.DEBUG,
        old_level=logging.INFO,
        steaming=True,
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

    # Регистрация хэндлеров
    register_common(dp)
    register_error(dp)

    # Регистрация middleware

    # Регистрация фильтров

    await dp.start_polling(bot, skip_updates=True)


def main():
    asyncio.run(start())
    asyncio.get_event_loop()


if __name__ == "__main__":
    main()
