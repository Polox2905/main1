from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions1 import *


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
bt1 = KeyboardButton(text="Рассчитать")
bt2 = KeyboardButton(text="Информация")
bt3 = KeyboardButton(text="Купить")
bt4 = KeyboardButton(text="Регистрация")

kb.add(bt1)
kb.add(bt2)
kb.add(bt3)
kb.add(bt4)

kbIn = InlineKeyboardMarkup()
btIn1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
btIn2 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
btIn3 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
btIn4 = InlineKeyboardButton(text='Product1', callback_data='product_buying')

kbIn.add(btIn1)
kbIn.add(btIn2)
kbIn.add(btIn3)
kbIn.add(btIn4)


class UserState(StatesGroup):
    cal = State()
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    st = State()
    username = State()
    email = State()
    age = State()

@dp.message_handler(text="Регистрация")
async def sign_up(message: types.Message):
    await message.answer('Введите имя пользователя (только латинский алфавит):"')
    await RegistrationState.st.set()


@dp.message_handler(text='Рассчитать')
async def calories(message: types.Message):
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


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    images = ['Images/im1.png', 'Images/im2.png', 'Images/im3.png', 'Images/im4.png']
    PRODUCTS = get_all_products()
    result = [(product['title'], product['description'], product['price']) for product in PRODUCTS]
    with open(images[0], "rb") as img1, \
            open(images[1], "rb") as img2, \
            open(images[2], "rb") as img3, \
            open(images[3], "rb") as img4:
        await message.answer(f'Название: {result[0][0]} | Описание: {result[0][1]} | Цена: {result[0][2]}')
        await message.answer_photo(img1)
        await message.answer(f'Название: {result[1][0]} | Описание: {result[1][1]} | Цена: {result[1][2]}')
        await message.answer_photo(img2)
        await message.answer(f'Название: {result[2][0]} | Описание: {result[2][1]} | Цена: {result[2][2]}')
        await message.answer_photo(img3)
        await message.answer(f'Название: {result[3][0]} | Описание: {result[3][1]} | Цена: {result[3][2]}')
        await message.answer_photo(img4)
    await message.answer('Выберите продукт для покупки:', reply_markup=kbIn)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(content_types=["text"])
async def not_start(message: types.Message):
    if message.text != '/start':
        await message.answer('Введите команду /start, чтобы начать общение.')


@dp.message_handler(state=RegistrationState.st)
async def set_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    username = message.text
    if not is_included(username):
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
    else:
        await message.answer("Пользователь с таким именем уже существует. Введите другое имя:")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_emai(message: types.Message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.update_data(email=message.text)
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    user_data = await state.get_data()
    username = user_data['username']
    email = user_data['email']
    age = message.text

    if age.isdigit():
        age = int(age)
        add_user(username, email, age)
        await message.answer(
            f"Учетная запись успешно зарегистрирована!\nИмя пользователя: {username}\nEmail: {email}\nВозраст: {age}"
        )
        await state.finish()
    else:
        await message.answer("Пожалуйста, введите корректный возраст.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)