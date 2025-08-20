from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.json_work import get_profiles
from app.keyboards import profile_for_id_keyboard

router = Router()


@router.callback_query(F.data.startswith("profile_"))
async def profile_for_id_handler(callback: CallbackQuery) -> None:
    """
        This handler sends profile for id
    """
    profiles = get_profiles()
    profile_id = int(callback.data.split("_")[1])
    await callback.answer("")
    await callback.message.edit_text(text=f"""Profile for id: {profile_id}
Name: {profiles[profile_id - 1]["name"]}
Age: {profiles[profile_id - 1]["age"]}
Status: {profiles[profile_id - 1]["status"]}
""", reply_markup=profile_for_id_keyboard)
