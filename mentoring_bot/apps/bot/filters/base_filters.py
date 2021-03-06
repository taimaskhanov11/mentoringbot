from aiogram import types
from aiogram.dispatcher.filters import BaseFilter
from loguru import logger

from mentoring_bot.db.models import User


class UserFilter(BaseFilter):
    async def __call__(self, update: types.CallbackQuery | types.Message) -> dict[str, User]:
        user = update.from_user
        user, is_new = await User.get_or_create(
            user_id=user.id,
            defaults={
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "language": user.language_code,
            },
        )
        data = {"user": user, "new_user": False}
        if is_new:
            data.update(new_user=True)
            logger.info(f"Новый пользователь {user=}")
        return data
