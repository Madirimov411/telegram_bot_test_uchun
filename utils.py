import os
from aiogram import Bot

TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_USERNAME = f"@{os.getenv('CHANNEL_ID')}"  # Kanal usernamesi

bot = Bot(token=TOKEN)

async def check_member(user_id):
    """Foydalanuvchining kanalga a'zo ekanligini tekshiradi"""













# from aiogram import Bot
# from aiogram.types import ChatMemberStatus
# import asyncio
#
# TOKEN = "YOUR_BOT_TOKEN"
# GROUP_ID = -1001234567890  # Guruh yoki kanal ID-si
#
# bot = Bot(token=TOKEN)
#
# async def check_membership(user_id):
#     """Foydalanuvchining guruh yoki kanalda borligini tekshiradi"""
#     try:
#         member = await bot.get_chat_member(GROUP_ID, user_id)
#
#         if member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
#             return True  # Foydalanuvchi guruh a'zosi
#         else:
#             return False  # Foydalanuvchi guruhda yo‘q
#
#     except Exception as e:
#         print(f"Xatolik: {e}")
#         return False  # Foydalanuvchini tekshirib bo‘lmadi
#
# # Asinxron funksiya ishlashini tekshirish
# async def main():
#     user_id = 123456789  # Tekshiriladigan foydalanuvchi ID-si
#     is_member = await check_membership(user_id)
#     print(f"Foydalanuvchi guruhda: {is_member}")
#
# asyncio.run(main())


