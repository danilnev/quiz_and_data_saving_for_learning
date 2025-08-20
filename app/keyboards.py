from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.json_work import get_profiles

main_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Заполнить анкету")],
        [KeyboardButton(text="Посмотреть мою анкету")],
        [KeyboardButton(text="Анкеты других людей")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие:",
    one_time_keyboard=True,
)

main_inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Наш сайт", url="https://google.com")]
        ]
    )

profile_for_id_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="back_to_profiles")]
    ]
)

async def inline_profiles():
    profiles = get_profiles()

    keyboard = InlineKeyboardBuilder()
    for profile in profiles:
        keyboard.add(InlineKeyboardButton(text=f"{profile["name"]}, {profile["age"]} years old", callback_data=f"profile_{profile['id']}"))
    return keyboard.adjust(1).as_markup()

