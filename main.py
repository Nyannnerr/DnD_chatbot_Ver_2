import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from src.python_bot.bot import DnDBot

# Load environment variables (.env or Replit Secrets)
load_dotenv()

# Setup Intents (cần thiết cho bot Discord hiện đại)
intents = discord.Intents.default()
intents.message_content = True # Cho phép bot đọc tin nhắn

# Khởi tạo Discord Bot và DnD Logic
bot = commands.Bot(command_prefix='!', intents=intents)
dnd_logic = DnDBot()

@bot.event
async def on_ready():
    print(f'Bot đã sẵn sàng! Đăng nhập dưới tên: {bot.user}')

# Các lệnh của bot
@bot.command()
async def start(ctx, player_id: str, scene_id: str):
    response = await dnd_logic.handle_start(player_id, scene_id)
    await ctx.send(response)

@bot.command()
async def status(ctx):
    response = await dnd_logic.handle_status()
    await ctx.send(response)

@bot.command()
async def attack(ctx, *, weapon: str):
    response = await dnd_logic.handle_attack(weapon)
    await ctx.send(response)

# Chạy bot
if __name__ == "__main__":
    token = os.environ.get('DISCORD_TOKEN')
    if not token:
        print("LỖI: Chưa cấu hình biến môi trường DISCORD_TOKEN.")
    else:
        bot.run(token)
