from statistics import mean

from aiogram import Dispatcher, F, Router, types
from aiogram.dispatcher.fsm.context import FSMContext

from mentoring_bot.apps.bot.markups.admin import admin_markups
from mentoring_bot.config.config import config
from mentoring_bot.db.models import Evaluation

router = Router()


async def admin_start(message: types.CallbackQuery | types.Message, state: FSMContext):
    await state.clear()
    if isinstance(message, types.CallbackQuery):
        message = message.message

    await message.answer("Админ панель", reply_markup=admin_markups.admin_start())


async def statistics(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    answer = "Пользователь - Оценка\n"
    evaluations = await Evaluation.all().select_related("user")
    evaluations_list = []
    for e in evaluations:
        answer += f"@{e.user.username} - {e.point}\n"
        evaluations_list.append(e.point)
    answer += f"\n📊 Средняя оценка:  {mean(evaluations_list)}"
    await call.message.answer(answer)


def register_admin(dp: Dispatcher):
    dp.include_router(router)
    router.message.filter(F.from_user.id.in_(config.bot.admins))

    callback = router.callback_query.register
    message = router.message.register

    message(admin_start, commands="admin", state="*")
    callback(admin_start, text="admin", state="*")
    callback(statistics, text="statistics", state="*")
