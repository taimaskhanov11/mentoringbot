from mentoring_bot.apps.bot.markups.utils import get_inline_keyboard, get_reply_keyboard, get_as_column, \
    get_inline_url_keyboard, get_inline_button
from mentoring_bot.loader import _


def start():
    keyboard = [
        ((_("Главное меню"), "menu"),),
    ]
    return get_inline_keyboard(keyboard)


def menu():
    keyboard = [
        "Расписание",
        "Новости обучения",
        "Связаться с преподавателем",
        "Посмотреть базу знаний",
        "Посмотреть уроки",
    ]
    return get_reply_keyboard(get_as_column(keyboard))


ui_url = "https://www.figma.com/file/tXNBWZqm71HmU1TFbXxaCn/%D0%91%D0%B0%D0%B7%D0%B0-" \
         "%D0%B7%D0%BD%D0%B0%D0%BD%D0%B8%D0%B9-%D0%BF%D0%BE-UI?node-id=0%3A1"
ux_url = "https://www.figma.com/file/153POhh2Ymc68NFLzCMapz/%D0%91%D0%B0%D0%B7%D0%B0" \
         "-%D0%B7%D0%BD%D0%B0%D0%BD%D0%B8%D0%B9-%D0%BF%D0%BE-UX?node-id=0%3A1"


def knowledge():
    keyboard = [
        ((_("База знаний по UI"), ui_url),),
        ((_("База знаний по UX"), ux_url),),
    ]
    keyboard = get_inline_url_keyboard(keyboard)
    keyboard.inline_keyboard.append(
        [get_inline_button(("⬅️Назад", "menu"))]
    )
    return keyboard


module1 = "https://lk.soultip.online/teach/control/stream/view/id/582373385"
module2 = "https://lk.soultip.online/teach/control/stream/view/id/582373390 "
module3 = "https://lk.soultip.online/teach/control/stream/view/id/582373387 "
module4 = "https://lk.soultip.online/teach/control/stream/view/id/582373388 "
module5 = "https://lk.soultip.online/teach/control/stream/view/id/582373389"


def lessons():
    keyboard = [
        (_("Модуль 1"), module1),
        (_("Модуль 2"), module2),
        (_("Модуль 3"), module3),
        (_("Модуль 4"), module4),
        (_("Модуль 5"), module5),
    ]
    keyboard = get_as_column(keyboard, col=2)
    keyboard = get_inline_url_keyboard(keyboard)
    keyboard.inline_keyboard.append(
        [get_inline_button(("⬅️Назад", "menu"))]
    )
    return keyboard


def deferred_message():
    keyboard = [
        (_("Смотреть видео-уроки"), "https://lk.soultip.online/"),
        (_("Отправить домашнее задание"), "https://t.me/katerinakriger"),
    ]
    keyboard = get_as_column(keyboard, col=1)
    keyboard = get_inline_url_keyboard(keyboard)
    keyboard.inline_keyboard.append(
        [get_inline_button(("⬅️Назад", "menu"))]
    )
    return keyboard
