import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/python_bot')))

from game_engine import GameEngine

# Khởi tạo engine
engine = GameEngine('data/scenes.json', 'data/players.json')

# Test đọc dữ liệu
player = engine.get_player('player_1')
scene = engine.get_scene('scene_001')

print(f"Player: {player['name']}, HP: {player['hp']}")
print(f"Scene: {scene['location']}, Difficulty: {scene['difficult']}")

# Test cập nhật HP
engine.update_player_hp('player_1', -20)
updated_player = engine.get_player('player_1')
print(f"Updated HP: {updated_player['hp']}")
