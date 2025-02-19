import asyncio
import logging
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

# 🔑 Token va ID larni olish
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_ID").replace("@", "")  # `@` belgisini olib tashlaymiz
ADMIN_ID = int(os.getenv("ADMIN_USER_ID"))

# 🤖 Botni ishga tushiramiz
bot = Bot(token=BOT_TOKEN, timeout=20)
dp = Dispatcher()

# 🔥 Logger
logging.basicConfig(level=logging.INFO)

# 📌 Foydalanuvchi sonini saqlash
user_count = 0
users_list = []


async def check_membership(user_id: int) -> bool:
    """Foydalanuvchining kanalga a'zo ekanligini tekshiradi."""
    try:
        member = await bot.get_chat_member(f"@{CHANNEL_USERNAME}", user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        logging.error(f"Xatolik: {e}")
        return False


@dp.message(Command("start"))
async def start_command(message: types.Message):
    """Foydalanuvchini kanalga a'zo ekanligini tekshirib, keyingi bosqichga yo‘naltiradi."""
    user_id = message.from_user.id

    # 🔍 A'zolikni tekshirish
    is_member = await check_membership(user_id)

    if is_member:
        # ✅ Kanalga a'zo bo‘lsa, menyuni ko‘rsatamiz
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🐍 Python"), KeyboardButton(text="💻 JavaScript"), KeyboardButton(text="💼 Java")],
                [KeyboardButton(text="💻 C++"), KeyboardButton(text="🟧 C#"), KeyboardButton(text="💼 GO")],
                [KeyboardButton(text="📘 TypeScript"), KeyboardButton(text="📓 Kotlin"), KeyboardButton(text="📖 PHP")],
                [KeyboardButton(text="📃 Bot haqida ma'lumot")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        response = f"👋 Assalomu alaykum {message.from_user.first_name}!\n\nBotga xush kelibsiz! Siz qaysi dasturlash tilini bilasiz?"
        await message.answer(response, reply_markup=keyboard)

        # 📊 Yangi foydalanuvchi statistikasi
        global user_count, users_list
        user_info = {
            "id": user_id,
            "ism": message.from_user.first_name,
            "familiya": message.from_user.last_name or "-",
            "username": message.from_user.username or "-",
            "vaqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        if user_info not in users_list:
            users_list.append(user_info)
            user_count = len(users_list)

            # 📩 Adminga xabar yuborish
            try:
                await bot.send_message(
                    ADMIN_ID,
                    f"👤 Yangi foydalanuvchi qo‘shildi!\n\n"
                    f"🆔 ID: {user_info['id']}\n"
                    f"👤 Ism: {user_info['ism']}\n"
                    f"📝 Familiya: {user_info['familiya']}\n"
                    f"🔗 Username: @{user_info['username']}\n"
                    f"⏳ Vaqt: {user_info['vaqt']}\n\n"
                    f"📊 Jami foydalanuvchilar: {user_count}"
                )
            except Exception as e:
                logging.error(f"Admin xabar yuborishda xatolik: {e}")

    else:
        # ❌ Kanalga a'zo bo‘lmagan bo‘lsa, a’zolik tekshiruv tugmasi bilan javob qaytaramiz
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📢 Kanalga a'zo bo‘lish", url=f"https://t.me/{CHANNEL_USERNAME}")],
            [InlineKeyboardButton("✅ A’zolikni tekshirish", callback_data="check_membership")]
        ])
        await message.answer(
            "⚠️ Botdan foydalanish uchun kanalga a'zo bo‘lishingiz kerak!\n\n"
            "👇 Pastdagi tugma orqali kanalga qo‘shiling va yana tekshiring:",
            reply_markup=keyboard
        )


@dp.callback_query(lambda c: c.data == "check_membership")
async def membership_callback(callback_query: CallbackQuery):
    """Foydalanuvchi kanalga a'zo ekanligini qaytadan tekshiradi."""
    user_id = callback_query.from_user.id
    is_member = await check_membership(user_id)

    if is_member:
        # ✅ Kanalga a'zo bo‘lsa, menu yuboramiz
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("🐍 Python"), KeyboardButton("💻 JavaScript"), KeyboardButton("💼 Java")],
                [KeyboardButton("💻 C++"), KeyboardButton("🟧 C#"), KeyboardButton("💼 GO")],
                [KeyboardButton("📘 TypeScript"), KeyboardButton("📓 Kotlin"), KeyboardButton("📖 PHP")],
                [KeyboardButton("📃 Bot haqida ma'lumot")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        await callback_query.message.answer(
            f"✅ Rahmat, {callback_query.from_user.first_name}! Siz kanalga a'zo ekansiz.\n\n"
            "Iltimos, kerakli dasturlash tilini tanlang:",
            reply_markup=keyboard
        )
    else:
        await callback_query.answer("❌ Siz hali ham kanalga a'zo bo‘lmagansiz! Iltimos, oldin qo‘shiling.", show_alert=True)


if __name__ == "__main__":
    print("🚀 Bot ishga tushirilmoqda...")
    asyncio.run(dp.start_polling(bot, skip_updates=True, timeout=30))
