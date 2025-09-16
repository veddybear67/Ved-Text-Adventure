class Character:
    def __init__(self, name, dialogue, is_enemy=False, item=None, weakness=None):
        self.name = name
        self.dialogue = dialogue
        self.is_enemy = is_enemy
        self.item = item
        self.weakness = weakness

    def talk(self):
        print(f"{self.name}: {self.dialogue}")

    def fight(self, weapon):
        if self.is_enemy:
            if weapon == self.weakness:
                print(f"You defeated {self.name} with the {weapon}!")
                return True
            else:
                print(f"{self.name} crushed you. You needed {self.weakness}.")
                return False
        else:
            print(f"{self.name} doesn’t want to fight.")
            return None
