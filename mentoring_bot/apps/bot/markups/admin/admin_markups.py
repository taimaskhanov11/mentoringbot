from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_start():
    builder = InlineKeyboardBuilder()
    builder.button(text="Статистика", callback_data="statistics")
    return builder.as_markup()
