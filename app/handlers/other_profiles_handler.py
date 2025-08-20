from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from ..keyboards import inline_profiles


router = Router()


@router.message(F.text == "Анкеты других людей")
async def other_profiles_handler(message: Message) -> None:
    """
        This handler sends list of profiles for picking
    """
    await message.answer(text="Выбери анкету для просмотра:", reply_markup=await inline_profiles())

@router.callback_query(F.data == "back_to_profiles")
async def back_to_profiles_handler(callback: CallbackQuery) -> None:
    """
        This handler sends list of profiles for picking
    """
    await callback.answer("")
    await callback.message.edit_text(text="Выбери анкету для просмотра:", reply_markup=await inline_profiles())
