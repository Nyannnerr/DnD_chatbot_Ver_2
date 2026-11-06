import sys
import os
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/python_bot')))

from bot import DnDBot

async def test_bot():
    bot = DnDBot()
    
    # Test !start
    print(await bot.handle_start('player_1', 'scene_001'))
    
    # Test !status
    print(await bot.handle_status())
    
    # Test !attack
    print(await bot.handle_attack(2))

asyncio.run(test_bot())
