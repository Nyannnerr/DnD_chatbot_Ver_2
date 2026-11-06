import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/python_bot')))

from game_engine import GameEngine
from gemini_client import GeminiClient

def test_new_features():
    engine = GameEngine('data/scenes.json', 'data/players.json', 'data/classes.json')
    
    # Test Class loading and Effective HP
    player = engine.get_player('player_1')
    eff_hp = engine.get_effective_hp('player_1')
    print(f"Player {player['name']} (Class: {player['class']}) - Effective HP: {eff_hp} (Base: {player['hp']} + Class Bonus)")
    gemini = GeminiClient()

    # Test Dice/Modifier
    engine.start_game('player_1', 'scene_001')
    dmg = engine.calculate_damage('player_1', 8, 'strength')
    print(f"Calculated Damage: {dmg} (Dice 1d8 + STR mod)")

    # Test Tools Mock
    print(gemini.handle_tool_call("spawn_enemy", {"enemy_type": "Goblin", "difficulty": 2}, engine))
    print(f"Active enemies: {engine.active_enemies}")

    # Test End Encounter
    print(gemini.handle_tool_call("end_encounter", {"result": "Victory"}, engine))
    print(f"Active enemies: {engine.active_enemies}")

test_new_features()
