import os
import asyncio
from src.python_bot.bot import DnDBot # Điều chỉnh import tùy theo cấu trúc thư mục của bạn

async def main():
    bot = DnDBot()
    # Nếu bạn dùng discord.py, hãy gọi bot.run(token) tại đây
    print("Bot đang chạy...")

if __name__ == "__main__":
    asyncio.run(main())
