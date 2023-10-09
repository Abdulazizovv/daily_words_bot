from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .is_admin import IsAdmin


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)

