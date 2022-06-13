import datetime

from aiogram import Dispatcher, Router, types, F
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import FSInputFile

from mentoring_bot.apps.bot.filters.base_filters import UserFilter
from mentoring_bot.apps.bot.handlers.temp import file_ids
from mentoring_bot.apps.bot.handlers.utils import create_deferred_message
from mentoring_bot.apps.bot.markups.common import common_markups
from mentoring_bot.config.config import MEDIA_DIR
from mentoring_bot.loader import _, scheduler

router = Router()


async def start(message: types.Message | types.CallbackQuery, new_user: bool, state: FSMContext):
    """Стартовое сообщение"""
    await state.clear()
    if isinstance(message, types.CallbackQuery):
        message = message.message
    if new_user:
        # создание отложенного сообщения для новых пользователей
        await create_deferred_message(message.from_user.id)


    await message.answer(_("Добро пожаловать в онлайн-школу дизайна Семена Романюка! "
                           "Мы рады приветствовать вас на нашем курсе по UI/UX дизайну. "
                           "В этом боте мы будем присылать вам напоминания о проведении онлайн-занятий, "
                           "а также вы можете ознакомиться с другими функциями нашего бота в главном меню"),
                         reply_markup=common_markups.menu())


async def menu(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    #await call.message.edit_reply_markup(common_markups.menu())
    await call.message.answer(_("Главное меню"), reply_markup=common_markups.menu())


async def schedule(message: types.Message):
    """Отправка расписания и сохранение id файла для последующей отправки"""
    program = "Программа курса.pdf"
    if program in file_ids:
        await message.answer_document(file_ids[program])
    else:
        await message.answer("Ваше обучение начинается с 13.06.2022 \n\n"
                             "Расписание по модулям курса:\n\n"
                             "◾️ 13.06 – модуль 1 (теория и практическое занятие)\n"
                             "◾️ 16.06 – разбор домашних заданий и практика\n"
                             "◾️ 20.06 – модуль 2 (теория и практическое занятие)\n"
                             "◾️ 23.06 – разбор домашних заданий и практика\n"
                             "◾️ 27.06 – модуль 3 (теория и практическое занятие)\n"
                             "◾️ 30.06 – разбор домашних заданий и практика\n"
                             "◾️ 04.07 – модуль 4 (теория и практическое занятие)\n"
                             "◾️️ 07.07 – разбор домашних заданий и практика\n"
                             "◾️ 11.07 – модуль 5 (теория и практическое занятие)\n\n"
                             "Более подробное описание вашей программы представлено в файле ниже👇 \n")
        message = await message.answer_document(FSInputFile(MEDIA_DIR / "Программа курса.pdf"))
        file_ids[program] = message.document.file_id


async def news(message: types.Message):
    """Новости обучения"""
    await message.answer("Мы будем присылать самые актуальные новости вам в наш чат-бот,"
                         "а пока вы можете посмотреть все свежие новости в нашем новостном канале👇\n\n"
                         "https://t.me/+D_316ATKGxdiMTVi")


async def teacher(message: types.Message):
    """Связаться с преподавателем"""
    await message.answer("Вы можете связаться с преподаваталем по ссылке, прикрепленной ниже.\n "
                        "Рабочие часы преподавателя по ответам ученикам: "
                         "ПН-ПТ с 12:00 до 18:00\n "
                         "СБ-ВСК – выходные дни\n "
                         "Связаться с преподавателем 👇\n "
                        "https://t.me/soultip ")

async def knowledge(message: types.Message):
    """Посмотреть базу знаний"""
    await message.answer("Выберите интересующую базу", reply_markup=common_markups.knowledge())


async def lessons(message: types.Message):
    """Посмотреть уроки"""
    await message.answer("Какой модуль вас интересует?", reply_markup=common_markups.lessons())


def register_common(dp: Dispatcher):
    dp.include_router(router)

    callback = router.callback_query.register
    message = router.message.register

    message(start, UserFilter(), commands="start", state="*")
    # callback(start, UserFilter(), text="menu", state="*")
    callback(menu, UserFilter(), text="menu", state="*")
    message(schedule, F.text.lower() == "расписание")
    message(news, F.text.lower() == "новости обучения")
    message(teacher, F.text.lower() == "связаться с преподавателем")
    message(knowledge, F.text.lower() == "посмотреть базу знаний")
    message(lessons, F.text.lower() == "посмотреть уроки")
