import datetime

from aiogram.utils import markdown

from mentoring_bot.apps.bot.markups.common import common_markups
from mentoring_bot.loader import bot, scheduler

url1 = markdown.hlink("Смотреть видео-уроки", "https://lk.soultip.online/")
url2 = markdown.hlink("Отправить домашнее задание", "https://t.me/katerinakriger ")

deferred_text = (
    "Для прохождения первого модуля “Технические основы UI/UX дизайна” "
    "Вам потребуется изучить видео-уроки модуля. "
    f"Для этого вы можете перейти в нашем боте по кнопке “{url1}”.\n\n"
    f"После прохождения модуля вам потребуется отправить домашнее задание по кнопке “{url2}”.\n"
    "В понедельник 13.06.2022 состоится наше первое занятие в онлайн-режиме."
    "Ниже мы отправляем ссылку-приглашение на конференцию. На онлайн-занятии мы разберем теорию на практике,"
    "а также разберем ваши домашние задания.\n\n"
    "Подключиться к конференции Zoom "
    "https://us04web.zoom.us/j/77766885613?pwd=XCeyhhWO4VcTqoweroTS8ltBLU8_oJ.1\n\n"
    "Идентификатор конференции: 777 6688 5613\n"
    "Код доступа: pQihh9"
)


async def send_deferred_message(user_id):
    """Отправка отложенного сообщения"""
    await bot.send_message(user_id, deferred_text, "html", reply_markup=common_markups.deferred_message())



async def create_deferred_message(user_id):
    """Создание отложенного сообщения"""
    new_date = datetime.datetime.now() + datetime.timedelta(hours=2)
    scheduler.add_job(send_deferred_message,
                      "date",
                      run_date=new_date,
                      args=[user_id])


async def part_sending(message, answer):
    if len(answer) > 4096:
        for x in range(0, len(answer), 4096):
            y = x + 4096
            await message.answer(answer[x:y])
    else:
        await message.answer(answer)
