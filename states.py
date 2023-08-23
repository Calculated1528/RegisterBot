from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileStatesGroup(StatesGroup):
    login_auth = State()
    pass_auth = State()
    login_reg = State()
    pass_reg = State()