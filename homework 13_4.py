from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    cal = State()
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(text='calories')
async def start(message: types.Message):
    await message.answer('Введите свой возраст')
    await UserState.cal.set()

@dp.message_handler(state=UserState.cal)
async def set_age(message: types.Message, state: FSMContext):
    await message.answer('Введите свой рост:')
    await state.update_data(age=message.text)
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await message.answer('Введите свой вес:')
    await state.update_data(growth=message.text)
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await UserState.weight.set()
    data = await state.get_data()
    print(data)
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    await message.answer(f'Норма калорий составляет {calories} ккал')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)













