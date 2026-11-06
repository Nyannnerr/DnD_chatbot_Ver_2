import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from src.python_bot.bot import DnDBot

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
dnd_logic = DnDBot()

@bot.event
async def on_ready():
    # Đồng bộ slash commands với Discord
    await bot.tree.sync()
    print(f'Bot đã sẵn sàng! Đăng nhập dưới tên: {bot.user}')

# Chuyển đổi sang Slash Commands
@bot.tree.command(name="start", description="Bắt đầu trò chơi với một scene")
async def start(interaction: discord.Interaction, scene_id: str):
    discord_player_id = str(interaction.user.id)
    response = await dnd_logic.handle_start(discord_player_id, scene_id)
    await interaction.response.send_message(response)

@bot.tree.command(name="status", description="Xem trạng thái hiện tại của bạn")
async def status(interaction: discord.Interaction):
    response = await dnd_logic.handle_status(str(interaction.user.id))
    await interaction.response.send_message(response)

@bot.tree.command(name="attack", description="Tấn công kẻ địch bằng vũ khí")
async def attack(interaction: discord.Interaction, weapon: str):
    response = await dnd_logic.handle_attack(str(interaction.user.id), weapon)
    await interaction.response.send_message(response)

if __name__ == "__main__":
    token = os.environ.get('DISCORD_TOKEN')
    if not token:
        print("LỖI: Chưa cấu hình DISCORD_TOKEN.")
    else:
        bot.run(token)
