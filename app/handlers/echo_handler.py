from aiogram import Router
from aiogram.types import Message 


router = Router()


@router.message()
async def echo_handler(message: Message) -> None:
    """
        This handler is called when user send any message
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
