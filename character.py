class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def describe(self):
        print(f"{self.name} is here! {self.description}")

    def talk(self):
        if self.conversation:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn’t want to talk.")


class Enemy(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, item):
        if item == self.weakness:
            print(f"You defeated {self.name} with {item}!")
            return True
        else:
            print(f"{self.name} crushed you! Game Over.")
            return False
