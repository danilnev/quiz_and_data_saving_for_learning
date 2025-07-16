import asyncio
import logging
import sys
from config import BOT_TOKEN, DEBUG

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
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>!", parse_mode=ParseMode.HTML)

@dp.message()
async def echo_handler(message: Message) -> None:
    """
        This handler is called when user send any message
    """
    print("ok")
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    try:
        # Initializing Bot with default properties
        bot = Bot(token=BOT_TOKEN, defaultd=DefaultBotProperties(parse_mode=ParseMode.HTML))

        # Running events dispatcher
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logging.info("Bot stopped")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())