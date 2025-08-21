import asyncio
import logging
import sys
from config import BOT_TOKEN, DEBUG

from app.handlers.echo_handler import router as echo_router
from app.handlers.other_profiles_handler import router as other_profiles_router
from app.handlers.profile_for_id_handler import router as profile_for_id_router
from app.handlers.fill_the_profile_fsm_handlers import router as fill_the_profile_router

from app.keyboards import main_keyboard, main_inline_keyboard

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


dp = Dispatcher()


@dp.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    """
        This handler is called when user use '/start' command
    """
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>!", parse_mode=ParseMode.HTML, reply_markup=main_keyboard)


async def main() -> None:
    # Initializing Bot with default properties
    bot = Bot(token=BOT_TOKEN, defaultd=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Registering routers
    # dp.include_router(echo_router)
    dp.include_router(other_profiles_router)
    dp.include_router(profile_for_id_router)
    dp.include_router(fill_the_profile_router)

    # Running events dispatcher
    await dp.start_polling(bot)


if __name__ == "__main__":
    if DEBUG == "True":
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
