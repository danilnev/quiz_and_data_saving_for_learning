from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.middlewares import TestMiddleware


router = Router()

router.message.middleware(TestMiddleware())


class FillTheProfileFSM(StatesGroup):
    name = State()
    number = State()
    age = State()
    status = State()


@router.message(F.text == "Заполнить анкету")
async def fill_the_profile(message: Message, state: FSMContext):
    await state.set_state(FillTheProfileFSM.name)
    await message.answer("Введите свое имя:")

@router.message(FillTheProfileFSM.name)
async def fill_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text.capitalize())
    await state.set_state(FillTheProfileFSM.number)
    await message.answer("Введите свой номер:")

@router.message(FillTheProfileFSM.number)
async def fill_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(FillTheProfileFSM.age)
    await message.answer("Введите свой возраст:")

@router.message(FillTheProfileFSM.age)
async def fill_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(FillTheProfileFSM.status)
    await message.answer("Введите статус:")

@router.message(FillTheProfileFSM.status)
async def fill_status(message: Message, state: FSMContext):
    await state.update_data(status=message.text)
    data = await state.get_data()
    await message.answer(f"""Спасибо! Анкета заполнена!
                         
Ваша анкета:
                         
Имя: {data["name"]}
Номер: {data["number"]}
Возраст: {data["age"]}
Статус: {data["status"]}
""")
    await state.clear()