import json
import os
import random
import math

class GameEngine:
    def __init__(self, scenes_path, players_path, classes_path):
        self.scenes_path = scenes_path
        self.players_path = players_path
        self.classes_path = classes_path
        self.scenes = self.load_json(scenes_path)
        self.players = self.load_json(players_path)
        self.classes = self.load_json(classes_path)

    def load_json(self, path):
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return {}
        with open(path, 'r') as f:
            return json.load(f)

    def roll_dice(self, sides):
        return random.randint(1, sides)

    def get_ability_modifier(self, score):
        return math.floor((score - 10) / 2)

    def calculate_damage(self, player_id, dice_type, modifier_type):
        player = self.players.get(player_id)
        if not player: return 0
        
        dice_roll = self.roll_dice(dice_type)
        modifier = self.get_ability_modifier(player.get(modifier_type, 10))
        return dice_roll + modifier

    def spawn_enemy(self, enemy_type, difficulty):
        enemy = {"type": enemy_type, "difficulty": difficulty, "hp": difficulty * 10}
        self.active_enemies.append(enemy)
        return f"Spawned {enemy_type} (Difficulty: {difficulty})"

    def trigger_ambush(self):
        return "Ambush triggered!"

    def end_encounter(self, result):
        self.active_enemies = []
        return f"Encounter ended. Result: {result}"

    def start_game(self, player_id, scene_id):
        if player_id in self.players:
            return self.get_scene(scene_id)
        return None

    def get_player(self, player_id):
        return self.players.get(player_id)

    def get_class_data(self, class_name):
        return self.classes.get(class_name)

    def get_class_trait(self, class_name):
        class_data = self.get_class_data(class_name)
        return class_data.get('trait', 'No special traits.')

    def get_effective_hp(self, player_id):
        player = self.get_player(player_id)
        if not player: return 0
        
        class_data = self.get_class_data(player['class'])
        bonus = class_data.get('hp_bonus', 0) if class_data else 0
        
        return player['hp'] + bonus

    def calculate_class_damage(self, player_id, damage):
        player = self.get_player(player_id)
        if not player: return damage
        
        if player['class'] == 'fighter':
            return damage + 2
        elif player['class'] == 'mage':
            return int(damage * 1.5)
        return damage

    def get_scene(self, scene_id):
        for scene in self.scenes:
            if scene['id'] == scene_id:
                return scene
        return None
