# character.py
class Character:
    def __init__(self, name, description="", dialogue=None):
        self.name = name
        self.description = description
        self.dialogue = dialogue or ""

    def talk(self):
        if self.dialogue:
            print(f"{self.name}: \"{self.dialogue}\"")
        else:
            print(f"{self.name} doesn't have anything to say.")


class Enemy(Character):
    def __init__(self, name, description="", dialogue=None, weakness=None, health=100, damage=10):
        super().__init__(name, description, dialogue)
        self.weakness = weakness      
        self.health = health
        self.damage = damage

    def fight(self, weapon_name):
        """Return True if defeated, False if player loses."""
        if weapon_name and weapon_name.lower() == (self.weakness or "").lower():
            print(f"You used {weapon_name}. It's super effective against {self.name}!")
            return True
        else:
            print(f"{self.name} laughs as your {weapon_name or 'bare hands'} fail to stop them.")
            return False

