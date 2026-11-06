from game_engine import GameEngine
from gemini_client import GeminiClient

class DnDBot:
    def __init__(self):
        self.engine = GameEngine('data/scenes.json', 'data/players.json', 'data/classes.json')
        self.gemini = GeminiClient()

    async def handle_start(self, player_id, scene_id):
        if self.engine.start_game(player_id, scene_id):
            player = self.engine.get_player(player_id)
            return f"Game started! Welcome {player['name']} the {player['class']}. Location: {self.engine.current_scene['location']}"
        return "Failed to start game."

    async def handle_status(self):
        if not self.engine.active_player_id:
            return "No active game."
        player = self.engine.get_player(self.engine.active_player_id)
        eff_hp = self.engine.get_effective_hp(self.engine.active_player_id)
        trait = self.engine.get_class_trait(player['class'])
        return f"Status: {player['name']} ({player['class']}), HP: {eff_hp}. Trait: {trait}"

    async def handle_attack(self, weapon_type):
        if not self.engine.active_player_id:
            return "No active game."
        
        player = self.engine.get_player(self.engine.active_player_id)
        class_data = self.engine.get_class_data(player['class'])
        
        modifier_type = 'strength' if class_data.get('is_melee') else 'dexterity'
        
        # Base damage
        damage = self.engine.calculate_damage(self.engine.active_player_id, 8, modifier_type)
        
        # Apply trait bonus (Simple simulation)
        if player['class'] == 'fighter':
            damage += 2
        elif player['class'] == 'mage':
            damage = int(damage * 1.5)
            
        narrative = self.gemini.generate_narrative(f"{player['name']} attacks with {weapon_type}")
        return f"{player['name']} attacked with {weapon_type}! Damage: {damage}. {narrative}"
