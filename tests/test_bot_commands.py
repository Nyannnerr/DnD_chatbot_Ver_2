import sys
import os
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/python_bot')))

from bot import DnDBot

async def test_commands():
    bot = DnDBot()
    
    # 1. Test !start
    print(await bot.handle_start('player_1', 'scene_001'))
    
    # 2. Test !status
    print(await bot.handle_status())
    
    # 3. Test !attack (fighter nên dùng strength)
    print(await bot.handle_attack('Longsword'))

asyncio.run(test_commands())
