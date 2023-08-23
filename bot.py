from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from db import Database
from config import TOKEN_API
from keyboard import get_kb
from messages import *
from states import ProfileStatesGroup


storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)

base = Database()

@dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=start_msg,
                           reply_markup=get_kb())
    if state is None:
        return
    await state.finish()


@dp.message_handler(content_types=['text'], state=ProfileStatesGroup.login_auth)
async def login_authorization(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text
        if (base.check_login(data['name'])):
            await ProfileStatesGroup.pass_auth.set()
            await bot.send_message(message.from_user.id, text=password)
        else:
            await bot.send_message(message.from_user.id, text=failed_auth)


@dp.message_handler(content_types=['text'], state=ProfileStatesGroup.pass_auth)
async def password_authorization(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['password'] = message.text

        if ((base.check_password(data['password'])) and (len(str(message.text)) == 8)):
            await bot.send_message(message.from_user.id, text=success_auth)
            await state.finish()
        else:
            await bot.send_message(message.from_user.id, text=failed_auth)


@dp.message_handler(content_types=['text'], state=ProfileStatesGroup.login_reg)
async def login_registration(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text
        if (base.check_login(data['name'])):
            await bot.send_message(message.from_user.id, text=failed_reg)
        else:
            await ProfileStatesGroup.pass_reg.set()
            await bot.send_message(message.from_user.id, text=password)


@dp.message_handler(content_types=['text'], state=ProfileStatesGroup.pass_reg)
async def password_registration(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['password'] = message.text
        if ((len(str(message.text)) == 8)):
            base.insert(data['name'], data['password'])
            await bot.send_message(message.from_user.id, text=success_reg)
            await state.finish()
        else:
            await bot.send_message(message.from_user.id, text=pass_warning)




@dp.callback_query_handler()
async def ikb_cb_handler(callback_query: types.CallbackQuery):
    if callback_query.data == 'btn_reg':
        await ProfileStatesGroup.login_reg.set()
        await bot.send_message(callback_query.from_user.id, text=login)
        await callback_query.message.delete()

    if callback_query.data == 'btn_auth':
        await ProfileStatesGroup.login_auth.set()
        await bot.send_message(callback_query.from_user.id, text=login)
        await callback_query.message.delete()




if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)